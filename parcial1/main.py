from negocio.evaluadorCredito import EvaluadorCredito
from datos.centralRiesgoSqlserver import CentralRiesgoSQLServer
from datos.repositorioSqlserver import RepositorioSQLServer
from presentacion.interfazConsola import InterfazConsola

def main():

    central = CentralRiesgoSQLServer()
    evaluador = EvaluadorCredito(central)
    interfaz = InterfazConsola()
    repo = RepositorioSQLServer()

    # Revisar que los datos se cargan desde SQL Server:
    solicitudes = repo.obtener_solicitudes()

    print("\nSolicitudes obtenidas de la base de datos:")
    print(len(solicitudes))

    for i in solicitudes:
        print(i)

    while True:

        solicitud = interfaz.obtener_solicitud()

        if solicitud is None:
            break

        resultado = evaluador.evaluar(solicitud)
        interfaz.mostrar_resultado(resultado)

        continuar = input("\n¿Desea realizar otra consulta? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()
