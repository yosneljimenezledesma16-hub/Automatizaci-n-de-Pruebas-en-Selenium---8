
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Abrir página de práctica
    driver.get("https://the-internet.herokuapp.com/login")

    # Localizar usuario y contraseña
    usuario = driver.find_element(By.ID, "username")
    clave = driver.find_element(By.NAME, "password")

    # Escribir los datos
    usuario.send_keys("tomsmith")
    clave.send_keys("SuperSecretPassword!")

    # Pulsar iniciar sesión
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Esperar el resultado
    resultado = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    print("Resultado del inicio de sesión:", resultado.text)

    input("Presiona ENTER para cerrar el navegador...")

finally:
    driver.quit()
