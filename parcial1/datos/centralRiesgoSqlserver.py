import pyodbc
from negocio.interfaces import ICentralRiesgo


class CentralRiesgoSQLServer(ICentralRiesgo):

    def __init__(self):

        self.connection_string = (
            "DRIVER={SQL Server};"
            "SERVER=LAPTOP-SQRL55HD\\SQLEXPRESS;"
            "DATABASE=usuarios;"
            "UID=sa;"
            "PWD=Solin1227;"
            "TrustServerCertificate=yes;"
        )

    def obtener_puntaje(self, documento: str):

        conn = pyodbc.connect(self.connection_string)

        cursor = conn.cursor()

        query = "SELECT puntaje FROM datos WHERE nroDocumento = ?"

        cursor.execute(query, documento)

        fila = cursor.fetchone()

        conn.close()

        if fila:
            return fila[0]

        return None
    