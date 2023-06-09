# Projeto para Sorteio

O projeto é baseado para que através de uma planilha em Excel as informação como número e nome na lista já preenchida, transcreve as informação da planilha para o navegador de forma automatizada usando Python 3.11 (funcionando somente no VS Code do Windows), inserindo e alocando as informação que ficam na pasta TEMP do próprio computador e não no navegador, esta interação não pesa sua internet e facilita que outros usuários possam usar simultâneamente em varios locais e sem a interferÊncia externas.

Porjeto ainda não foi aplicado para linux, no momento estou desenvolvendo um código, tendo em vista que no momento a ferramento PYAUTOGUI que usa a extensão TKinter não se aplica a versão VS Code do linux.

# Ferramentas Adicionais para que funcione:

Será preciso instalar algumas ferramentas e extensões para que rode o código com precisão, segue abaixo aalgumas delas inclusives estão disponíveis em projetos da comunidade aqui no GitHub:

Selenium WebDriver usei várias referências diferentes:

- 1 API do WebDriver: https://selenium-python.readthedocs.io/api.html

- 2 Selenium IDE e Grid: https://www.selenium.dev/documentation/webdriver/browsers/

- 3 Gerenciamento do WebDriver via Python: https://pypi.org/project/webdriver-manager/

PyAutoGui: https://pypi.org/project/PyAutoGUI/

TKinter: https://docs.python.org/3/library/tk.html

GeckoDriver: https://github.com/mozilla/geckodriver/releases

OpenPyXl: https://pypi.org/project/openpyxl/

# Instalando Ferramentas Adicionais:

Primeiro antes de começar tudo certifique-se que consta em seu computador instalado a programa VS Code e a versão correto do Python conforme imagem abaixo.

![image](https://github.com/alvaciroliveira/rifa/assets/129803614/5b45b320-445e-4afd-baae-d2326a558c1c)

 - Prontos então vamos lá . . .

Abra o VS Code, vá até o terminal conforme imagem abaixo e instale as seguintes ferramentas:
![image](https://github.com/alvaciroliveira/rifa/assets/129803614/f79803a7-3b57-4157-b4ab-c2566a689513)

```bash
pip3 install openpyxl pyaautogui selenium
```

Instalando TKinter dentro do VS Code no Windows, vá até em externsões conforme imagem abaixo e instale o TKinter:
![image](https://github.com/alvaciroliveira/rifa/assets/129803614/28222746-8933-46ec-95df-2dcbcb6acdc5)

Tudo pronto após colocar todas as referências não se esqueça de efetuar a instalação do GeckoDriver (*.exe) em local fácil em sua maquina, seguindo os passos de colocar o PATH do GeckoDrive nas váriaveis de ambiente do Windows.

Usando primeiro a versão de teste (testefirefox.py) e dando tudo certo, usando a versão recente do Firefox, agora pode executar o teste:

Usando o navegador do Firefox, baixe o arquivo e faça os testes: https://github.com/alvaciroliveira/rifa/blob/main/testefirefox.py

 - Lembrando dentro do arquivo possuem nome e números somente como referência caso queira, sabendo o que vai fazer pode ser alterados.

# Usando a Versão Final

Certifique que a sua planilha do Excel já esta em local correto e que já efetuou as alterações de onde a mesma estão localizadas efetue o VS Code e na dúvida estou a disposicão.

Sorteio: https://github.com/alvaciroliveira/rifa/blob/main/firefox.py

