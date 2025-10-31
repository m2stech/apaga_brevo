from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

# Carrega variáveis de ambiente
load_dotenv()

# Configuração
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Login
    print("Acessando Brevo...")
    driver.get("https://login.brevo.com/")
    
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys(os.getenv("BREVO_EMAIL"))
    print("Email preenchido")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(os.getenv("BREVO_PASSWORD"))
    print("Senha preenchida")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-button']")
    login_button.click()
    print("Login realizado! Aguardando 60 segundos...")
    time.sleep(60)
    
    # Ir para contatos
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    contatos_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Ir para Contatos']")))
    contatos_link.click()
    print("Clicou em 'Ir para Contatos'")
    
    # Loop de exclusão
    ciclo = 1
    while True:
        try:
            print(f"\n=== CICLO {ciclo} ===")
            time.sleep(5)
            
            # Configurar 100 por página
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            pagination_button = wait.until(EC.element_to_be_clickable((By.ID, "pagination-selector-rows-per-page__trigger")))
            pagination_button.click()
            time.sleep(2)
            
            option_100 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='100']")))
            option_100.click()
            print("100 contatos por página")
            time.sleep(5)
            
            # Selecionar todos
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(2)
            
            checkbox_all = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mfe-app-container']/div/div/main/div[1]/div[2]/article/div[2]/table/thead[2]/tr/th[1]/span/div/label/span[1]")))
            checkbox_all.click()
            print("Todos selecionados")
            time.sleep(3)
            
            # Mais ações
            mais_acoes_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='moreActionBtn']")))
            mais_acoes_btn.click()
            time.sleep(2)
            
            # Excluir
            excluir_btn = wait.until(EC.element_to_be_clickable((By.ID, "deleteAction")))
            excluir_btn.click()
            time.sleep(3)
            
            # Confirmar com 100
            input_confirmacao = wait.until(EC.presence_of_element_located((By.ID, "sib-delete-input")))
            input_confirmacao.send_keys("100")
            
            botao_excluir_final = wait.until(EC.element_to_be_clickable((By.ID, "cont-deleteAction-save")))
            botao_excluir_final.click()
            print("Excluindo...")
            
            # Aguardar e refresh
            time.sleep(10)
            driver.refresh()
            print("Página atualizada")
            
            ciclo += 1
            
        except Exception as e:
            print(f"Fim dos contatos ou erro: {e}")
            break
    
    print("Todos os contatos foram deletados!")
    input("Pressione Enter para fechar...")
    
except Exception as e:
    print(f"Erro: {e}")
    
finally:
    driver.quit()
