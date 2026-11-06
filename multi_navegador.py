
from selenium import webdriver
import sys

navegador = sys.argv[1].lower() if len(sys.argv) > 1 else "chrome"

if navegador == "chrome":
    driver = webdriver.Chrome()

elif navegador == "firefox":
    driver = webdriver.Firefox()

elif navegador == "edge":
    driver = webdriver.Edge()

else:
    raise ValueError("Navegador no reconocido")

try:
    driver.get("https://www.selenium.dev/")

    print("Navegador:", navegador)
    print("Título:", driver.title)
    print("URL:", driver.current_url)

    input("Presiona ENTER para cerrar...")

finally:
    driver.quit()
