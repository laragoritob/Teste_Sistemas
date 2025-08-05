from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com o protocólo file://
# Certifique-se de que o carrinho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/lara_g_souza/TESTE_DE_SISTEMAS/login.html")

# Preenche o campo Nome
usuario_input = driver.find_element(By.ID, "usuario")
usuario_input.send_keys("admin")

# Preenche o campo CPF
senha_input = driver.find_element(By.ID, "senha")
senha_input.send_keys("123456")

# Clica no botão de cadastro
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Aguarda alguns segundos para verificar o resultado
time.sleep(5)

# Fecha o navegador
driver.quit()