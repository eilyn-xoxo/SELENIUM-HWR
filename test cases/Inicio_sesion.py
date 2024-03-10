from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configuración inicial
url = "https://www.udemy.com"
usuario = "eilynfortunaperezramirez@gmail.com"
contraseña = "Contraseña123!"

# Iniciar el navegador
driver = webdriver.Chrome()
driver.get(url)

# Pasos del caso de prueba
driver.get ('https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F')
time.sleep(4)  # Esperar a que se cargue la página de inicio de sesión

# Ingresar nombre de usuario y contraseña
driver.find_element_by_name("email").send_keys(usuario)
driver.find_element_by_name("password").send_keys(contraseña)

# Hacer clic en el botón de inicio de sesión
driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()
time.sleep(2)  # Esperar a que se complete el inicio de sesión

# Verificar resultados esperados
if "dashboard" in driver.current_url:
    print("Inicio de sesión exitoso. Prueba PASADA.")
else:
    print("Inicio de sesión fallido. Prueba FALLADA.")

# Cerrar el navegador
driver.quit()
