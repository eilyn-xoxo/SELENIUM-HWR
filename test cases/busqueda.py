from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Opciones del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Ejecutar en segundo plano

# Ruta al driver de Chrome
driver = webdriver.Chrome()

# URL de Platzi
url = 'https://platzi.com/'

# Acceder a la página
driver.get(url)

# Buscar el campo de búsqueda
campo_busqueda = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'autocomplete-8-label'))
)

# Introducir el término de búsqueda
campo_busqueda.send_keys('Python')


# Esperar a que se carguen los resultados
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="SearchPage-resultsList"]'))
)

# Obtener los títulos de los cursos
titulos_cursos = driver.find_elements(By.CSS_SELECTOR, 'h3[class="CardItem-title"]')

# Imprimir los títulos de los cursos
for titulo in titulos_cursos:
    print(titulo.text)

# Cerrar el navegador
driver.quit()


# Verificar que se muestran resultados de búsqueda
assert "Resultados para " + search_query in driver.page_source

# Mostrar títulos de los cursos encontrados
course_titles = driver.find_elements_by_class_name("MaterialCard-title")
print("Cursos encontrados:")
for title in course_titles:
    print("- " + title.text)

# Cerrar el navegador
driver.close()
