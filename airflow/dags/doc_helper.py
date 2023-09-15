import psycopg2

# PostgreSQL connection details creds are from airflow docker-compose file
host = "postgres13"
port = "5432"  
database = "veryfidev"
user = "airflow"
password = "airflow"

def current_max_document_id():
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    cursor = conn.cursor()

    try:
        query = "SELECT MAX(document_id) FROM documents;"
        cursor.execute(query)
        max_document_id = cursor.fetchone()[0]

    except (Exception, psycopg2.Error) as error:
        print("Error while reading data:", error)

    finally:
        cursor.close()
        conn.close()

    return max_document_id

def read_document_rows(start_document_id, end_document_id, page_size):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()

    query = """
    SELECT *
    FROM documents
    WHERE document_id BETWEEN %s AND %s
    ORDER BY document_id ASC
    LIMIT %s
    """
    values = (start_document_id, end_document_id, page_size)

    cursor.execute(query, values)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
