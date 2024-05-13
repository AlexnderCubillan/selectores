from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Configuración inicial de Selenium (asegúrate de tener el controlador de Chrome o Firefox)
driver = webdriver.Chrome()  # O webdriver.Firefox()

# Abre una página web
driver.get('https://www.google.com/')

# Localizador del elemento (puedes usar diferentes estrategias)
#localizador = (By.ID, 'element_id')  # Cambia 'element_id' por el ID real del elemento
# Otros ejemplos:
localizador = (By.XPATH, '/HTML/BODY/DIV/DIV[2]/DIV/IMG')
# localizador = (By.CLASS_NAME, 'button-class-name')

try:
    # Encuentra el elemento
    elemento = driver.find_element(*localizador)

    # Haz clic en el elemento
    elemento.click()

    print(f"Se hizo clic en el elemento con localizador {localizador}")
except Exception as e:
    print(f"Error al hacer clic: {e}")
finally:
    time.sleep(5)
    driver.quit()