from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from warnings import filterwarnings

filterwarnings("ignore")

# Configura automáticamente el driver de Chrome
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# Abrir la página
browser.get('https://resultadodelaloteria.com/')

# Buscar el elemento con el ID 'ctl00_ulColombia'
resultList = browser.find_element(By.ID, 'ctl00_ulColombia')

# Obtener todos los enlaces dentro del elemento
linkList = resultList.find_elements(By.TAG_NAME, 'a')

# Imprimir nombre y enlace
for link in linkList:
    print("Nombre: %s / Link: %s" % (link.text, link.get_attribute('href')))

# Cerrar el navegador
browser.quit()
