from gerenciador import GerenciadorDeNotificacoes
from notificador import Notificador

# Classe fake para simular um notificador durante os testes
class NotificadorFake(Notificador):
    def __init__(self):
        self.enviado = False  # Flag para verificar se o método enviar foi chamado
    
    def enviar(self, mensagem):
        # Marca como enviado se a mensagem não for vazia
        if len(mensagem) > 0:
            self.enviado = True

# Função de teste para verificar se o gerenciador chama o método enviar de todos os notificadores
def teste_gerenciador_de_notificacoes_enviar_todos():
    n1 = NotificadorFake()  # Primeiro notificador fake
    n2 = NotificadorFake()  # Segundo notificador fake

    gerenciador = GerenciadorDeNotificacoes([n1, n2])  # Cria o gerenciador com os dois notificadores
    gerenciador.enviar_todos("test")  # Envia uma mensagem de teste

    assert n1.enviado is True   # Verifica se o primeiro notificador recebeu a mensagem
    assert n2.enviado is True   # Verifica se o segundo notificador recebeu a mensagem