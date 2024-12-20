# Python Script for Prenotami scheduling and telegram notification

This is a python script to check the availability of schedule for the Italian consulate, more specifically, for the citizenship service, it's recommended to use the Prenotami link that you receive on your e-mail, otherwise you will need to alter the **Prenotami.py code** to fit your needs.

After checking the availability it will generate a telegram message through a telegram bot, check [official documentation] (https://core.telegram.org/bots) to how to set your own bot.

1. Create a copy from **.env** and replace the placeholder with your own information
2. Install requirements.txt file
3. Running:
    1. You can manually run the **main.py** file for local execution (selenium configuration is for running using headless chrome, not necessary to install WebDriver)
    2. Run **docker build and run**, this will set the cronjob to execute every 30 min
