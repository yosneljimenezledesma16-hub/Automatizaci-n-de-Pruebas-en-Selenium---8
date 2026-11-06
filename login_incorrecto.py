
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("usuario_falso")
    driver.find_element(By.NAME, "password").send_keys("clave_falsa")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    resultado = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    print("Resultado:", resultado.text)

    if "Your username is invalid!" in resultado.text:
        print("PRUEBA APROBADA: Selenium detectó el error correctamente.")
    else:
        print("PRUEBA NO APROBADA.")

    input("Presiona ENTER para cerrar...")

finally:
    driver.quit()
