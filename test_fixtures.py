
from selenium.webdriver.common.by import By

def test_pagina(driver):

    driver.get("https://the-internet.herokuapp.com")

    titulo = driver.find_element(
        By.TAG_NAME, "h1"
    ).text

    assert titulo == "Welcome to the-internet"

    print("PRUEBA CON FIXTURE APROBADA")
