from negocio.entidades import SolicitudCredito
from negocio.evaluadorCredito import EvaluadorCredito
from datos.centralRiesgoSqlserver import CentralRiesgoSQLServer

def ejecutar_pruebas():

    central = CentralRiesgoSQLServer()

    evaluador = EvaluadorCredito(central)

    casos = [
        SolicitudCredito("12345678", 5000000, 2000000, 10000000, 12),
        SolicitudCredito("1026131420", 2000000, 1000000, 3000000, 12),
        SolicitudCredito("1036448588", 4000000, 2000000, 5000000, 24),
        SolicitudCredito("99999999", 5000000, 2000000, 5000000, 12)
    ]

    for i, caso in enumerate(casos, 1):

        resultado = evaluador.evaluar(caso)

        estado = "APROBADO" if resultado.aprobado else "RECHAZADO"

        print(f"Prueba {i}: {estado} -> {resultado.motivo}")


if __name__ == "__main__":
    ejecutar_pruebas()
