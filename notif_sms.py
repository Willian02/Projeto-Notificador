from notificador import Notificador

# Notificador que envia mensagens por SMS
class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f"[SMS] {mensagem}")
