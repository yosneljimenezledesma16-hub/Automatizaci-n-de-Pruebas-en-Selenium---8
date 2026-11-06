
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # PRUEBA 1: Manejar ventanas
    driver.get("https://the-internet.herokuapp.com/windows")

    ventana_original = driver.current_window_handle

    driver.find_element(By.LINK_TEXT, "Click Here").click()

    wait.until(EC.number_of_windows_to_be(2))

    nueva_ventana = next(
        ventana for ventana in driver.window_handles
        if ventana != ventana_original
    )

    driver.switch_to.window(nueva_ventana)

    print("Nueva ventana:", driver.find_element(By.TAG_NAME, "h3").text)

    driver.close()
    driver.switch_to.window(ventana_original)

    print("PRUEBA DE VENTANAS APROBADA")

    # PRUEBA 2: Manejar frames
    driver.get("https://the-internet.herokuapp.com/iframe")

    wait.until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, "mce_0_ifr")
        )
    )

    editor = driver.find_element(By.ID, "tinymce")

    print("Contenido del frame:", editor.text)

    driver.switch_to.default_content()

    print("PRUEBA DE FRAMES APROBADA")

    input("Presiona ENTER para cerrar...")

finally:
    driver.quit()
