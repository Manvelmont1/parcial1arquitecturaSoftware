import pyodbc
from negocio.entidades import SolicitudCredito

class RepositorioSQLServer:

    def __init__(self):

        self.connection_string = (
            "DRIVER={SQL Server};"
            "SERVER=LAPTOP-SQRL55HD\\SQLEXPRESS;"
            "DATABASE=usuarios;"
            "UID=sa;"
            "PWD=Solin1227;"
            "TrustServerCertificate=yes;"
        )

    def obtener_solicitudes(self):

        conexion = pyodbc.connect(self.connection_string)
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT 
                tipoDocumento,
                nroDocumento,
                ingresosTotales,
                egresosTotales,
                montoSolicitado,
                plazoSolicitado
            FROM datos
        """)

        solicitudes = []

        for row in cursor.fetchall():

            solicitud = SolicitudCredito(

                documento=str(row.nroDocumento),
                ingresos=int(row.ingresosTotales),
                egresos=int(row.egresosTotales),
                monto=int(row.montoSolicitado),
                plazo=int(row.plazoSolicitado)

            )

            solicitudes.append(solicitud)

        conexion.close()

        return solicitudes
