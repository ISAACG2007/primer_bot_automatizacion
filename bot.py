from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Usar la versión correcta automáticamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abre Google
driver.get("https://www.google.com")

# Esperar 2 segundos y buscar algo
time.sleep(2)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hola mundo bot")
search_box.submit()

# Esperar para ver resultados
time.sleep(5)
driver.quit()
