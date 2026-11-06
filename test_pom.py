
from selenium import webdriver
from pagina_login import PaginaLogin

driver = webdriver.Chrome()

try:
    pagina = PaginaLogin(driver)

    pagina.abrir()

    pagina.iniciar_sesion(
        "tomsmith",
        "SuperSecretPassword!"
    )

    mensaje = pagina.obtener_mensaje()

    print("\nMENSAJE:", mensaje)

    assert "You logged into a secure area!" in mensaje

    print("\nPRUEBA POM APROBADA")


except Exception as error:
    print("ERROR EN LA PRUEBA:", error)
    input("Presiona ENTER para cerrar...")

finally:
    driver.quit()
