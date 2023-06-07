from selenium import webdriver
import pandas as pd
import time
import urllib.parse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path=r'C:\Users\Ângelo Miguel\AppData\Local\Programs\Python\Python311\geckodriver-v0.33.0-win32\geckodriver.exe')
    
contatos_df = pd.read_excel("Enviar.xlsx")

driver.get("https://web.whatsapp.com/")

while len (driver.find_elements(By.ID, 'side')) < 1:
    time.sleep(10)
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa  = contatos_df.loc[i,"Pessoa"]
    numero = contatos_df.loc[i,"Número"]
    texto = urllib.parse.quote(f"{pessoa} ,{mensagem}")
    link  = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    driver.get(link)
    while len (driver.find_elements(By.ID, 'side')) < 1:
        time.sleep(10)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="compose-btn-send"]')))
    driver.execute_script("arguments[0].click();", button)
    time.sleep(30)

