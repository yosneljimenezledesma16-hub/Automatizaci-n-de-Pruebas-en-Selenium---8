
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com")

    # Ejecutar JavaScript
    titulo = driver.execute_script(
        "return document.title;"
    )

    print("Título mediante JavaScript:", titulo)

    # Crear una cookie
    driver.add_cookie({
        "name": "mi_cookie",
        "value": "prueba_selenium"
    })

    # Consultar las cookies
    cookies = driver.get_cookies()

    print("\nCookies encontradas:")

    for cookie in cookies:
        print(cookie["name"], "=", cookie["value"])

    # Comprobar nuestra cookie
    assert any(
        cookie["name"] == "mi_cookie"
        for cookie in cookies
    )

    print("\nPRUEBA DE COOKIES APROBADA")
    print("PRUEBA DE JAVASCRIPT APROBADA")

    input("Presiona ENTER para cerrar...")

finally:
    driver.quit()
