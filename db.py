import psycopg2
def get_connection():
   return psycopg2.connect(
        host="localhost",
        database="tryhospitaldb",
        user="postgres",
        password="ramadan1111"
    )
