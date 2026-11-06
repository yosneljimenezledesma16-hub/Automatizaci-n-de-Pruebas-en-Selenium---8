
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_pagina_principal():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com")

        assert "The Internet" in driver.title

        print("PRUEBA APROBADA")

    finally:
        driver.quit()


def test_titulo_pagina():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com")

        titulo = driver.find_element(
            By.TAG_NAME, "h1"
        ).text

        assert titulo == "Welcome to the-internet"

        print("TITULO CORRECTO")

    finally:
        driver.quit()
