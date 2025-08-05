from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuração do WebDriver (nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

# Acessa a página de cadastro usando o caminho absoluto com o protocólo file://
# Certifique-se de que o carrinho está apontando para um arquivo HTML específico

driver.get("file:///C:/Users/lara_g_souza/TESTE_DE_SISTEMAS/produto.html")

# Preenche o campo id
id_input = driver.find_element(By.ID, "id")
id_input.send_keys("3")

# Preenche o campo desc
desc_input = driver.find_element(By.ID, "desc")
desc_input.send_keys("Celular")

# Preenche o campo marca
marca_input = driver.find_element(By.ID, "marca")
marca_input.send_keys("Xiaomi")

# Preenche o campo quantidade
quantidade_input = driver.find_element(By.ID, "qntd")
quantidade_input.send_keys("4")

quantidade_input = driver.find_element(By.ID, "preco")
quantidade_input.send_keys("2000")

# Clica no botão de cadastro
# cadastro_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# cadastro_button.click()

# Aguarda alguns segundos para verificar o resultado
time.sleep(8)

# Fecha o navegador
driver.quit()