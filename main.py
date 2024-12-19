from SeleniumService import Driver
from Prenotami import RunPrenotami
from TelegramService import TelegramBot
import os
from datetime import datetime

if __name__ == "__main__":
	MainDriver = Driver(60)
	MainDriver.Login()

	bot = TelegramBot()
	if RunPrenotami(MainDriver):
		bot.send_message(f"Agendamento pode estar diponivel, acessar {os.getenv('URL_SERVICO')} para tentar realizar o agendamento")
	else:
		bot.send_message(f"Agendamento ainda indisponivel!")
		#pass
	print(f"{datetime.now()} - Run finish with sucess, verify telegram chat to check status!")

	MainDriver.Dispose()
