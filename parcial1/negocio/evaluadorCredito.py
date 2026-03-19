from .entidades import Resultado
from .interfaces import IEvaluadorCredito, ICentralRiesgo

class EvaluadorCredito(IEvaluadorCredito):

    def __init__(self, central: ICentralRiesgo):
        self.central = central

    def evaluar(self, s):

        # Revisar plazo:
        if s.plazo < 1 or s.plazo > 72:
            return Resultado(False, "Plazo inválido. Debe estar entre 1 y 72 meses")

        # Balanza:
        balanza = s.balanza()

        if balanza <= 0:
            return Resultado(False, f"Balanza negativa o cero ({balanza})")

        # Relación credito balanza:
        relacion = s.relacion()

        # Rechazar solicitud:
        if relacion >= 0.95:
            return Resultado(
                False,
                f"Relación crédito/balanza demasiado alta ({relacion:.3f})"
            )


        # Puntajes:
        if 0.7 <= relacion < 0.95:
            minimo = 800
        elif 0.4 <= relacion < 0.7:
            minimo = 600
        else:
            minimo = 400

        puntaje = self.central.obtener_puntaje(s.documento)

        if puntaje is None:
            return Resultado(False, "Documento no encontrado en central de riesgo")

        # Aprobar:
        aprobado = puntaje >= minimo
        estado = "APROBADO" if aprobado else "RECHAZADO"

        motivo = (
            f"{estado} - "
            f"Balanza: {balanza:.2f} | "
            f"Relación: {relacion:.3f} | "
            f"Puntaje: {puntaje} | "
            f"Mínimo requerido: {minimo}"
        )
        return Resultado(aprobado, motivo, puntaje)
