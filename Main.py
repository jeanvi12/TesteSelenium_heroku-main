from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:\\Users\\LabJF\\Downloads\\chromedriver-win32 (2)\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://the-internet.herokuapp.com/key_presses?")

    def enviarDados(usuario):
        
        btn_login = WebDriverWait(driver, 10).until (
            EC.presence_of_element_located((By.XPATH, '//*[@id="target"]'))
        )
        btn_login.clear()
        btn_login.send_keys(usuario)
        driver.implicitly_wait(5)  
        alert = driver.find_element(By.ID, "result").text
        return alert
    
    alert = enviarDados(Keys.F1)
    print(alert)
    if 'You entered: F1' in alert :
        print("Teste de usuário inválido bem sucedido")
    else:
        print("Usuário incorreto não reconhecido, teste falhou")
    
    alert = enviarDados(Keys.F3)
    print(alert)
    if 'You entered: F3' in alert :
        print("Teste de usuário inválido bem sucedido")
    else:
        print("Usuário incorreto não reconhecido, teste falhou")

    alert = enviarDados(Keys.DELETE)
    print(alert)
    if 'You entered: DELETE' in alert:
        print("Teste de tecla bem sucedido")
    else:
        print("Falha mostrar tecla, teste falhou")

    print("Todos os testes concluídos com sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()