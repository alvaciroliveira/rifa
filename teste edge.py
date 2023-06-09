import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = '~/edgedriver_win32'
options = webdriver.EdgeOptions()
driver = webdriver.Edge(executable_path=driver_path, options=options)
driver.get("https://meykillo.blogspot.com")

# Lista de nomes e números
nomes = ["nome-1", "nome-2", "nom-3", "nome-4", "nome-5", "nome6"]

numeros = ["1", "2", "3", "4", "5", "6"]


# Copia as informações e transcreve na ordem
for i in range(1, 1001):
    nome = nomes[i-1]
    numero = numeros[i-1]

    pyautogui.click(x=100, y=200)
    pyautogui.press('tab')
    pyautogui.press('delete')

    input_nome = driver.find_element(By.ID, "name")
    input_nome.send_keys(nome)

    pyautogui.doubleClick(x=320, y=430)
    pyautogui.press('delete')
    pyautogui.press('tab')
    
    element = driver.find_element(By.ID, "number")
    element.send_keys(numero)
    pyautogui.click(x=319, y=465)

    # Simula o clique no botão "Participar da Rifa"
pyautogui.click(x=319, y=465)
