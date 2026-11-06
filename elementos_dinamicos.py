
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    print("Esperando que aparezca el elemento...")

    # Pulsar el botón Start
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # Esperar hasta que el resultado sea visible
    resultado = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    print("Resultado:", resultado.text)
    print("PRUEBA APROBADA: elemento dinámico encontrado.")

    input("Presiona ENTER para cerrar...")

finally:
    driver.quit()
