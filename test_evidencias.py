
def test_pagina(driver):

    driver.get("https://the-internet.herokuapp.com")

    titulo = driver.title

    assert titulo == "Titulo incorrecto"
