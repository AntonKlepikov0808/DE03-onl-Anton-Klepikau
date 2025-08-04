import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123",
        host="localhost",
        port=5432
    )
    print("к базе данных.")

   
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print("PostgreSQL:", db_version[0])

    # Закрытие
    cur.close()
    conn.close()

except Exception as e:
    print(" Ошибка:", e)
