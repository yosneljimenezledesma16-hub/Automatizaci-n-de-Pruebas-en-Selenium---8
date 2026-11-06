
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaginaLogin:

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(
            "https://the-internet.herokuapp.com/login"
        )

    def iniciar_sesion(self, usuario, clave):

        self.driver.find_element(
            By.ID, "username"
        ).send_keys(usuario)

        self.driver.find_element(
            By.ID, "password"
        ).send_keys(clave)

        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        ).click()

    def obtener_mensaje(self):

        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "flash")
            )
        )

        return elemento.text
