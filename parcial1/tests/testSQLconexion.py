import pyodbc

connection_string = (
    "DRIVER={SQL Server};"
    "SERVER=LAPTOP-SQRL55HD\\SQLEXPRESS;"
    "DATABASE=usuarios;"
    "UID=sa;"
    "PWD=Solin1227;"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(connection_string)
    print("Conectado a la DataBase.")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM datos")

    total = cursor.fetchone()[0]
    print("Total de registros en la tabla datos: ", total)

    conn.close()

except Exception as e:
    print("Error al conectar: ", e)
