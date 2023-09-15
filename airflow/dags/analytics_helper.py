import json
import psycopg2
import doc_helper
import dag_progress_helper

# PostgreSQL connection details creds are from airflow docker-compose file
host = "postgres13"
port = "5432"  
database = "veryfidev"
user = "airflow"
password = "airflow"

class DocsAggregated:
    def __init__(self, document_count, total, score, ocr_score):
        self.document_count = document_count
        self.total = total
        self.score = score
        self.ocr_score = ocr_score
    def __str__(self):
        return f"DocsAggregated(document_count='{self.document_count}', total={self.total}, score='{self.score}, ocr_score='{self.ocr_score}')"

def get_documents(start_document_id, end_document_id, page_size):
    rows = doc_helper.read_document_rows(start_document_id, end_document_id, page_size)
    documents = []
    for row in rows:
        document_id, ml_response = row
        document = {
            'document_id': document_id,
            'ml_response': json.loads(ml_response)
        }
        documents.append(document)
    return documents

def retrieve_all_documents(start_document_id, end_document_id):
    page_size = 1000
    documents = []

    # Retrieve documents in chunks using the specified page size
    for page_start in range(start_document_id, end_document_id + 1, page_size):
        page_end = min(page_start + page_size - 1, end_document_id)
        results = get_documents(page_start, page_end, page_size)
        documents.extend(results)
    return documents

def generate_docs_aggregated(docs):
    document_count = 0
    total = 0
    score = 0
    ocr_score = 0
    for doc in docs:
        if doc:
            document_count += 1
            total += doc['ml_response']['total']['value']
            score += doc['ml_response']['total']['score']
            ocr_score += doc['ml_response']['total']['ocr_score']

    return DocsAggregated(document_count, total, score, ocr_score)

def generate_docs_aggregated_by_business_id(docs):
    docs_by_business = {};
    for doc in docs:
        business_id = doc['ml_response']['business_id']
        if business_id in docs_by_business:
            docs_by_business[business_id].append(doc)
        else:
            docs_by_business[business_id] = [doc]

    agg_by_business_id = {};
    for business_id, docs in docs_by_business.items():
        agg_by_business_id[business_id] = generate_docs_aggregated(docs)

    return agg_by_business_id

def upsert_business_analytics(business_id, grand_total, document_count, score_total, ocr_score_total):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()

    upsert_query = """
        WITH upsert AS (
            UPDATE business_analytics
            SET grand_total = business_analytics.grand_total + %s,
                document_count = business_analytics.document_count + %s,
                score_total = business_analytics.score_total + %s,
                ocr_score_total = business_analytics.ocr_score_total + %s
            WHERE business_id = %s
            RETURNING *
        )
        INSERT INTO business_analytics (business_id, grand_total, document_count, score_total, ocr_score_total)
        SELECT %s, %s, %s, %s, %s
        WHERE NOT EXISTS (SELECT * FROM upsert)
    """

    cursor.execute(
        upsert_query,
        (grand_total, document_count, score_total, ocr_score_total, business_id,
         business_id, grand_total, document_count, score_total, ocr_score_total)
    )

    conn.commit()

    cursor.close()
    conn.close()
    
def update_analytics(dag_id, execution_date):
    start_document_id = 0
    max_processed_doc_id = dag_progress_helper.max_processed_document_id()
    if max_processed_doc_id:
        start_document_id = max_processed_doc_id + 1

    current_max_doc_id = doc_helper.current_max_document_id()
    print("exectution_date:" + str(execution_date))
    print("max processed doc id:" + str(max_processed_doc_id))
    print("start doc id:" + str(start_document_id))
    print("max doc id:" + str(current_max_doc_id))

    if start_document_id <= current_max_doc_id:
        dag_progress_helper.create_dag_exec_progress(dag_id=dag_id, execution_date=execution_date, start_document_id=start_document_id, end_document_id=current_max_doc_id)

        docs = retrieve_all_documents(start_document_id, current_max_doc_id)
        summery_by_business = generate_docs_aggregated_by_business_id(docs)

        for business_id, docs_aggregated in summery_by_business.items():
            print(f"business_id {business_id}, doc agg: {docs_aggregated}")
            upsert_business_analytics(business_id=business_id, grand_total=docs_aggregated.total, document_count=docs_aggregated.document_count, score_total=docs_aggregated.score, ocr_score_total=docs_aggregated.ocr_score)

        dag_progress_helper.completed_dag_exec_progress(dag_id=dag_id, execution_date=execution_date)
