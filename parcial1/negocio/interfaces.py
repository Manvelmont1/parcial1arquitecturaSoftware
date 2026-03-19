from abc import ABC, abstractmethod


class IEvaluadorCredito(ABC):

    @abstractmethod
    def evaluar(self, solicitud):
        pass


class ICentralRiesgo(ABC):

    @abstractmethod
    def obtener_puntaje(self, documento: str):
        pass
