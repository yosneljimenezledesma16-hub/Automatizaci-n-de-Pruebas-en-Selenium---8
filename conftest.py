
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    yield navegador
    navegador.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call" and reporte.failed:

        navegador = item.funcargs.get("driver")

        if navegador:
            nombre = f"error_{item.name}.png"
            navegador.save_screenshot(nombre)

            print(f"Captura guardada: {nombre}")
