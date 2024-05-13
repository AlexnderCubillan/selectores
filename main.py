from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pynput.mouse import Listener as MouseListener
import keyboard
import sys

# Configuración inicial de Selenium
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# Lista para almacenar los detalles de los elementos
element_details_list = []

# Función para obtener los detalles de un elemento dado su posición x, y
def get_element_details_by_position(x, y):
    details = driver.execute_script("""
        var elem = document.elementFromPoint(arguments[0], arguments[1]);
        if (elem) {
            return {
                xpath: getElementXPath(elem),
                cssSelector: elem.tagName.toLowerCase() + (elem.id ? '#' + elem.id : '') + (elem.className ? '.' + elem.className.split(' ').join('.') : ''),
                className: elem.className,
                id: elem.id,
                linkText: elem.tagName.toLowerCase() === 'a' ? elem.innerText : null
            };
        }
        function getElementXPath(elt){
            var path = '';
            for (; elt && elt.nodeType == 1; elt = elt.parentNode){
                idx = getElementIdx(elt);
                xname = elt.tagName;
                if (idx > 1) xname += '[' + idx + ']';
                path = '/' + xname + path;
            }
            return path;
        }
        function getElementIdx(elt){
            var count = 1;
            for (var sib = elt.previousSibling; sib ; sib = sib.previousSibling){
                if(sib.nodeType == 1 && sib.tagName == elt.tagName) count++;
            }
            return count;
        }
    """, x, y)
    return details

# Función para manejar los eventos de clic del mouse
def on_click(x, y, button, pressed):
    if pressed:
        details = get_element_details_by_position(x, y)
        if details:
            element_details_list.append(details)
            print(f"Elemento clickeado: XPATH: {details['xpath']}, CSS_SELECTOR: {details['cssSelector']}, CLASS_NAME: {details['className']}, ID: {details['id']}, LINK_TEXT: {details['linkText']}")
        else:
            print("No se encontró ningún elemento en la posición dada.")

# Iniciar el listener del mouse
listener = MouseListener(on_click=on_click)
listener.start()

# Bucle para mantener el programa en ejecución hasta que se presione Escape
try:
    while True:
        if keyboard.is_pressed('esc'):
            print("\nSe presionó Escape, finalizando el programa...")
            print("\nDetalles de los elementos generados:")
            for i, details in enumerate(element_details_list, start=1):
                print(f"Elemento {i}: XPATH: {details['xpath']}, CSS_SELECTOR: {details['cssSelector']}, CLASS_NAME: {details['className']}, ID: {details['id']}, LINK_TEXT: {details['linkText']}")
            driver.quit()
            sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
finally:
    listener.stop()
    driver.quit()
