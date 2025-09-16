from abc import ABC, abstractmethod

# Classe abstrata base para notificadores
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass