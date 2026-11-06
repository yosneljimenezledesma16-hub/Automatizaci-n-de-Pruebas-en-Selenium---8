
import pytest
from selenium import webdriver

def test_captura_error():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com")

        assert "Texto incorrecto" in driver.title

    except AssertionError:
        driver.save_screenshot("error_prueba.png")
        raise

    finally:
        driver.quit()
