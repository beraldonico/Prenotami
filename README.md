# Python Script for Prenotami scheduling and telegram notification

This is a python script to check the disponibility of schedule for the italian consulate, more specifically, for the citizenship service, it's recomended to use the Prenotami link that you receive on your e-mail, other wise you will need to alter the **Prenotami.py code** to fit your needs.

After checking the disponibility it will generate a telegram message through a telegram bot, check [oficial documentantion](https://core.telegram.org/bots) to how to set your own bot.

1. Create a copy from **.env** and replace the placeholder with your own information
2. Install requirements.txt file
3. Running:
	1. You can manually run the **main.py** file for local execution(selenium configuration is for running using headless chrome, not necessary to install webdriver)
	2. Run **docker build and run**, this will set the cronjob to execute every 30 min

