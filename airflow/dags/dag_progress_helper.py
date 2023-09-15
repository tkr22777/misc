import psycopg2

# PostgreSQL connection details creds are from airflow docker-compose file
host = "postgres13"
port = "5432"  
database = "veryfidev"
user = "airflow"
password = "airflow"

def max_processed_document_id(): 
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    cursor = conn.cursor()

    try:
        query = "SELECT MAX(end_document_id) FROM dag_progress;"
        cursor.execute(query)
        max_end_document_id = cursor.fetchone()[0]

    except (Exception, psycopg2.Error) as error:
        print("Error while reading data:", error)

    finally:
        cursor.close()
        conn.close()

    return max_end_document_id

def create_dag_exec_progress(dag_id, execution_date, start_document_id, end_document_id):
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO dag_progress (dag_id, execution_date, start_document_id, end_document_id)
    VALUES (%s, %s, %s, %s)
    """
    data = (dag_id, execution_date, start_document_id, end_document_id)

    cursor.execute(insert_query, data)
    connection.commit()

    cursor.close()
    connection.close()

def completed_dag_exec_progress(dag_id, execution_date):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    
    cursor = conn.cursor()
    
    # Define the SQL query to update the end_date field
    query = """
        UPDATE dag_progress
        SET end_date = current_timestamp
        WHERE dag_id = %s
        AND execution_date = %s
    """
    
    cursor.execute(query, (dag_id, execution_date))
    
    conn.commit()
    
    cursor.close()
    conn.close()