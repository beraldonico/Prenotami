from SeleniumService import Driver
from Prenotami import RunPrenotami
from TelegramService import TelegramBot
import os
from datetime import datetime

if __name__ == "__main__":
	try:
		MainDriver = Driver(60)

		Service_avaiable = RunPrenotami(MainDriver)

		if Service_avaiable:
			bot = TelegramBot()
			bot.send_message(f"Agendamento pode estar diponivel, acessar {os.getenv('URL_SERVICO')} para tentar realizar o agendamento")
		else:
			bot = TelegramBot()
			bot.send_message(f"Agendamento ainda indisponivel!")
			#pass
		
		MainDriver.Dispose()
		print(f"{datetime.now().strftime(f"%Y/%m/%d %H:%M:%S")} - Process finish with sucess status! The avaiability of the service is {Service_avaiable}")
	except Exception as Ex:
		bot = TelegramBot()
		if Ex == "Unavailable":
                        bot.send_message(f"Site esta bloquando o acesso do bot, desligar servico por um tempo!")
		elif Ex == "Login Problem":
			bot.send_message(f"Problema ao tentar realizar login no site!")
		else:
			bot.send_message(f"Problema desconhecido: {Ex}")
		print(f"{datetime.now().strftime(f"%Y/%m/%d %H:%M:%S")} - Process finish with fail status! Exception: {Ex}")
