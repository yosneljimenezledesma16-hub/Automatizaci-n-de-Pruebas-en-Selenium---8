
from selenium import webdriver

# Abrir Google Chrome
driver = webdriver.Chrome()

try:
    # Visitar una página web
    driver.get("https://www.selenium.dev/")

    # Mostrar información
    print("Título de la página:", driver.title)
    print("Dirección web:", driver.current_url)

    # Mantener el navegador abierto
    input("Presiona ENTER para cerrar el navegador...")

finally:
    driver.quit()
