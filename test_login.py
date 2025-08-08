from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com o protocólo file://
# Certifique-se de que o carrinho está apontando para um arquivo HTML específico

driver.get("http://localhost:8080/TESTE_DE_SISTEMAS/login.html")

# Preenche o campo Nome
# usuario_input = driver.find_element(By.ID, "usuario")
# usuario_input.send_keys("admin")

# Preenche o campo CPF
# senha_input = driver.find_element(By.ID, "senha")
# senha_input.send_keys("123456")

# Clica no botão de cadastro
# login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# login_button.click()

# Preenche o campo Nome
driver.find_element(By.ID, "usuario").send_keys("admin")

# Preenche o campo CPF
driver.find_element(By.ID, "senha").send_keys("123456")

# Clica no botão de cadastro
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Aguarda alguns segundos para verificar o resultado
time.sleep(5)

if "Cadastro de Cliente" in driver.page_source:
    print("Login realizado com sucesso!")
else:
    print("Erro ao realizar o login.")

# Fecha o navegador
# driver.quit()