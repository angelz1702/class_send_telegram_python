# class_send_telegram_python
class to send message to telegram (https://core.telegram.org/bots/api)


use:

from TelegramMessage import TelegramMessage

TelegramMessage = TelegramMessage("path/historiques-soldes.dat")
message_status_action = ""


to add message to resume :

message_status_action = message_status_action + "your text here"


to send message 

TelegramMessage.sendMessageResume(usdBalance, message_status_action, "title " )



