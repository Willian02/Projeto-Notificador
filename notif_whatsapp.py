from notificador import Notificador

# Notificador que envia mensagens por WhatsApp
class NotificadorWhatsapp(Notificador):
    def enviar(self, mensagem):
        print(f"[WHATSAPP] {mensagem}")