
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from SeleniumService import Driver
import os

def RunPrenotami(SeleniumDriver: Driver) -> bool:
	available: bool = False

	try:
		SeleniumDriver.Login()
	except:
		raise Exception("Login Problem")

	try:
		SeleniumDriver.wait.until(EC.presence_of_element_located((By.XPATH, os.getenv("XPATH_STRING_UNAVAILABLE"))))
		raise Exception("Unavailable")
	except TimeoutException:
		pass
	except Exception as Ex:
		raise Ex

	try:
		SeleniumDriver.wait.until(EC.presence_of_element_located((By.XPATH, os.getenv("XPATH_STRING"))))
	except TimeoutException:
		available = True
	except Exception as Ex:
		raise Ex
	
	return available
