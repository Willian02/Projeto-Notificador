from notificador import Notificador

# Gerenciador que envia notificações usando múltiplos notificadores
class GerenciadorDeNotificacoes:
    def __init__(self, notificadores: list[Notificador]):
        self.notificadores = notificadores
    
    # Envia a mensagem usando todos os notificadores fornecidos
    def enviar_todos(self, mensagem):
        for notificador in self.notificadores:
            notificador.enviar(mensagem)