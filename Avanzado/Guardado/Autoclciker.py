import pyautogui
import pyautogui as pag
import random
import time
import PySimpleGUI as sg
import tkinter as tk

pyautogui.FAILSAFE = False

layout =[
            [sg.Text("Autoclicker 0.1")],
            [sg.Button("Start")],
            [sg.Button("Stop")],
        ]
window = sg.Window("Autoclicker", layout)
x = 0

is_running = False
while True:
    event,values = window.Read()

    if event == "Start":
        is_running = True
        while is_running == True:
            pag.click()
            x += 1
            print(x)
    if event == "Stop":
        is_running = False



"""while True:
    x = random.randint(0,1080)
    y = random.randint(0,1920)
    pag.moveTo(x,y,0)
    time.sleep(1)"""