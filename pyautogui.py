# Com este código o "pyautogui" pode ajudar a ajustar com o mouse irá fica ao executar a informação desejada
import pyautogui

# Aguarde alguns segundos antes de executar o código abaixo
# Isso dará tempo para você posicionar o cursor do mouse onde deseja obter as coordenadas

# Obter as coordenadas do ponto atual do mouse
current_position = pyautogui.position()

# Imprimir as coordenadas na tela
print("Coordenadas: ", current_position)