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
	except:
		print(f"{datetime.now().strftime(f"%Y/%m/%d %H:%M:%S")} - Process finish with fail status!")
