
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("url, texto_esperado", [
    (
        "https://the-internet.herokuapp.com",
        "Welcome to the-internet"
    ),
    (
        "https://www.selenium.dev",
        "Automate any browser, from any language."
    )
])


def test_titulos(url, texto_esperado):

    driver = webdriver.Chrome()

    try:
        driver.get(url)

        encabezado = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                (By.TAG_NAME, "h1")
            )
        )

        texto = encabezado.text.strip()

        print("\nURL:", driver.current_url)
        print("TITULO:", driver.title)
        print("TEXTO ENCONTRADO:", texto)
        print("TEXTO ESPERADO:", texto_esperado)

        assert texto_esperado.lower() in texto.lower(), (
            f"Se esperaba '{texto_esperado}', "
            f"pero se encontro '{texto}'"
        )

    finally:
        driver.quit()
