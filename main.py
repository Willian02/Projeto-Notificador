from notif_email import NotificadorEmal
from notif_sms import NotificadorSMS
from notif_whatsapp import NotificadorWhatsapp
from notif_log import NotificadorLog
from gerenciador import GerenciadorDeNotificacoes

# Instancia os notificadores
email = NotificadorEmal()
sms = NotificadorSMS()
whatsapp = NotificadorWhatsapp()
log = NotificadorLog()

# Cria o gerenciador com todos os notificadores e envia uma mensagem
gerenciador = GerenciadorDeNotificacoes([email, sms, whatsapp, log])
gerenciador.enviar_todos("Mensagem enviada com sucesso")