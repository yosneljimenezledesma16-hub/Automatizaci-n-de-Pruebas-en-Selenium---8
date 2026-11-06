
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    # 1. Buscar por ID
    usuario = driver.find_element(By.ID, "username")
    print("ID:", usuario.get_attribute("id"))

    # 2. Buscar por NAME
    clave = driver.find_element(By.NAME, "password")
    print("NAME:", clave.get_attribute("name"))

    # 3. Buscar por CLASS
    boton = driver.find_element(By.CLASS_NAME, "radius")
    print("CLASS:", boton.text)

    # 4. Buscar por CSS SELECTOR
    css = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    print("CSS:", css.text)

    # 5. Buscar por XPATH
    xpath = driver.find_element(
        By.XPATH, "//button[@type='submit']"
    )
    print("XPATH:", xpath.text)

    print("PRUEBA APROBADA: todos los elementos fueron encontrados.")

    input("Presiona ENTER para cerrar...")

finally:
    driver.quit()
