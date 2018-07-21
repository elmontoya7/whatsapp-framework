from app.mac import mac, signals

'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.message_received.connect
def handle(message):
    print(message)
    mac.send_message("recibido", message.conversation)
