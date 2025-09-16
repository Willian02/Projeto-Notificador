from notificador import Notificador

# Notificador que envia mensagens por e-mail
class NotificadorEmal(Notificador):
    def enviar(self, mensagem):
        print(f"[EMAIL] {mensagem}")