from dataclasses import dataclass
from typing import Optional

@dataclass
class SolicitudCredito:
    documento: str
    ingresos: float
    egresos: float
    monto: float
    plazo: int

    def balanza(self) -> float:
        return self.ingresos - self.egresos

    def relacion(self) -> float:
        balanza = self.balanza()
        return float('inf') if balanza <= 0 else (self.monto / self.plazo) / balanza


@dataclass
class Resultado:
    aprobado: bool
    motivo: str
    puntaje: Optional[int] = None
