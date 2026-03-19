from negocio.entidades import SolicitudCredito


class InterfazConsola:

    def obtener_solicitud(self):

        print("Solicitud de credito".center(50, "-"))

        documento = input("Documento: ")
        ingresos = float(input("Ingresos mensuales: "))
        egresos = float(input("Egresos mensuales: "))
        monto = float(input("Monto solicitado: "))
        plazo = int(input("Plazo (meses): "))

        return SolicitudCredito(
            documento,
            ingresos,
            egresos,
            monto,
            plazo
        )

    def mostrar_resultado(self, resultado):

        print("\nResultado de la verificacion: ")

        if resultado.aprobado:
            print("Aprobado.")
        else:
            print("Rechazado.")

        print(resultado.motivo)
        print("\n".center(50, "-"))
