import openpyxl # Responsável para abrir excel e coleta de informações
import pyautogui # Responsável para que haja interação do mouse no projeto (Mão consegui usar em linux)
from selenium import webdriver # Responsável para abrir Firefox e coleta de informações
from selenium.webdriver.firefox.options import Options # Responsável por interação do navegador com GeckoDriver
from selenium.webdriver.common.by import By # Responsável por interação com navegador para coletar onde serão inserido as informações
from selenium.webdriver.common.keys import Keys # Responsável por interação do excel para o site transcrevendo informações

# Carregar o arquivo da planilha
workbook = openpyxl.load_workbook("C:/Users/Usuario/Desktop/Rifas.xlsx") # Substitua pelo caminho na qual a planilha esta localizada

# Selecionar a planilha desejada (tabela por exemplo)
worksheet = workbook['Rifa']

# Configurar as opções do navegador Firefox
driver_path = 'C:/Users/Usuario/Downloads/geckodriver-v0.33.0-win32' # Substitua pelo caminho na qual a pasta do "Geckodriver" (*.exe) esta localizada
options = Options()
options = webdriver.FirefoxOptions()

# Inicializar o driver do Firefox
driver = webdriver.Firefox(executable_path=driver_path, options=options)

# Abrir a página web no Firefox (Esta projeto consta este site construído para teste)
driver.get("https://meykillo.blogspot.com") # Substitua pela URL correta da página onde você deseja colar os valores

# Inicializar aplicação no navegador Firefox dentro da pagina agora já aberta
for index, row in enumerate(worksheet.iter_rows(values_only=True), start=1):
    # Ignorar a primeira linha (cabeçalho na tabela)
    if index == 1:
        continue
    numero = str(row[0])  # Coluna A (número)
    nome = str(row[1])  # Coluna B (nome)

    # Esta referência de código apaga informação anterior para que seja preenchida novamente com o Nome
    pyautogui.click(x=100, y=200)
    pyautogui.press('tab')
    pyautogui.press('delete')
    
    # Aqui o código para transcrever as informações Nome do participante da rifa
    input_nome = driver.find_element(By.ID, "name")    
    input_nome.send_keys(nome)

    # Esta referência de código apaga informação anterior para que seja preenchida novamente com o Número
    pyautogui.doubleClick(x=320, y=430)
    pyautogui.press('delete')
    pyautogui.press('tab')
    
    # Aqui o código para transcrever as informações Número do participante da rifa    
    element = driver.find_element(By.ID, "number")
    element.send_keys(numero)

    # Aqui o código valida Nome e Número do participante da rifa  
    pyautogui.click(x=319, y=465)
# Aqui o código valida o loop do processo anterior, confirmando que acabaram os participantes da rifa 
pyautogui.click(x=319, y=465)

# Código acaba aqui fica somente o processo manual que o usuário click no botaão "Sortear" no navegador 