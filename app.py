import pyautogui
import keyboard
import webbrowser
import win32api
import win32con
from time import sleep


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


webbrowser.open_new_tab('https://gameforge.com/en-US/littlegames/piano-tiles-3/#')  # noqa: E501;

try:
    sleep(4)
    pyautogui.locateCenterOnScreen('img/logo_site.png')
except pyautogui.ImageNotFoundException:
    botao_iniciar = pyautogui.locateCenterOnScreen('img/icone_iniciar.png')
    pyautogui.moveTo(botao_iniciar[0], botao_iniciar[1], duration=2)
    pyautogui.move(85, 0, duration=2)
    pyautogui.click()

    sleep(4)
    aba_site = pyautogui.locateCenterOnScreen('img/janela_site.png')
    pyautogui.moveTo(aba_site[0], aba_site[1], duration=2)
    pyautogui.click()

try:
    sleep(4)
    botao_fechar = pyautogui.locateCenterOnScreen('img/fechar_pop_up.png')
    pyautogui.moveTo(botao_fechar[0], botao_fechar[1], duration=2)
    pyautogui.click()
except pyautogui.ImageNotFoundException:
    pass

sleep(4)
botao_iniciar_jogo = pyautogui.locateCenterOnScreen('img/iniciar_jogo.png')
pyautogui.moveTo(botao_iniciar_jogo[0], botao_iniciar_jogo[1], duration=2)
pyautogui.click()

while keyboard.is_pressed('1') is False:
    if not pyautogui.pixelMatchesColor(454, 324, (215, 141, 255)):
        click(454, 324)
        sleep(0.01)
    if not pyautogui.pixelMatchesColor(508, 323, (215, 179, 255)):
        click(508, 323)
        sleep(0.01)
    if not pyautogui.pixelMatchesColor(562, 315, (215, 187, 255)):
        click(562, 315)
        sleep(0.01)
    if not pyautogui.pixelMatchesColor(627, 326, (211, 169, 255)):
        click(627, 326)
        sleep(0.01)
