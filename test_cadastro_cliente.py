from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com o protocólo file://
# Certifique-se de que o carrinho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/lara_g_souza/TESTE_DE_SISTEMAS/index.html")

# Preenche o campo Nome
nome_input = driver.find_element(By.ID, "name")
nome_input.send_keys("João da Silva")

# Preenche o campo CPF
cpf_input = driver.find_element(By.ID, "cpf")
cpf_input.send_keys("12345678901")

# Preenche o campo Endereço
endereco_input = driver.find_element(By.ID, "address")
endereco_input.send_keys("Rua das Flores, 123")

# Preenche o campo Telefone
telefone_input = driver.find_element(By.ID, "phone")
telefone_input.send_keys("11987654321")

# Clica no botão de cadastro
cadastro_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
cadastro_button.click()

# Aguarda alguns segundos para verificar o resultado
time.sleep(8)

# Fecha o navegador
driver.quit()