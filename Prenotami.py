
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from SeleniumService import Driver
import os

def RunPrenotami(SeleniumDriver: Driver) -> bool:
	available: bool = False

	try:
		SeleniumDriver.Login()
	except:
		raise Exception("Login Problem")

	try:
		SeleniumDriver.wait.until(EC.presence_of_element_located((By.XPATH, "//body[contains(text(),'Unavailable')]")))
		raise Exception("Unavailable")
	except:
		pass

	try:
		SeleniumDriver.wait.until(EC.presence_of_element_located((By.XPATH, os.getenv("XPATH_STRING"))))
	except:
		available = True
	finally:
		return available
