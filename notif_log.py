from notificador import Notificador

# Notificador que registra mensagens em um arquivo de log
class NotificadorLog(Notificador):
    def enviar(self, mensagem):
        with open("log.txt", "a") as f:
            f.write(f"[LOG] {mensagem}\n")