from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class Driver ():
	def __init__(self, TimeoutSeconds : int = None):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--disable-blink-features=AutomationControlled")
		chrome_options.add_argument("--headless=new") 
		chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
		#chrome_options.add_argument("--log-level=1")
		#chrome_options.add_argument("--no-sandbox")
		#chrome_options.add_argument("--disable-dev-shm-usage")
		#chrome_options.add_argument("--disable-gpu")

		webdriver_service = Service(ChromeDriverManager().install())

		self.driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

		if TimeoutSeconds:
			self.wait = WebDriverWait(self.driver, TimeoutSeconds)	

	def WaitTime(self, TimeoutSeconds: int):
		self.wait = WebDriverWait(self.driver, TimeoutSeconds)

	def Dispose(self):
		self.driver.quit()

	def Login(self):
		self.driver.get(os.getenv("URL_SERVICO"))
	
		Element = self.wait.until(EC.presence_of_element_located((By.XPATH, os.getenv("XPATH_USER"))))
		Element.send_keys(os.getenv("LOGIN_USER"))

		Element = self.wait.until(EC.presence_of_element_located((By.XPATH, os.getenv("XPATH_PASSWORD"))))
		Element.send_keys(os.getenv("LOGIN_PASSWORD"))

		Element = self.wait.until(EC.presence_of_element_located((By.XPATH, os.getenv("XPATH_LOGIN_BUTTON"))))
		Element.click()

if __name__ == "__main__":
	DriverTester = Driver(10)
	DriverTester.Get("Insert URL")
	
	Element = DriverTester.wait.until(EC.presence_of_element_located((By.ID, "login-password")))
	Element.send_keys("text")

	Element = DriverTester.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-form']/button")))
	Element.click()

	DriverTester.Dispose()