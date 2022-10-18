# https://www.classicgame.com/game/Whack+a+Mole

#imports
from turtle import Screen
from classes.ScreenReader import ScreenReader
from re import template
import cv2
import pyautogui
import os
import numpy as np
import time
from time import sleep
import logging

startTime = time.time()

os.chdir(os.path.dirname(os.path.abspath(__file__)))
cv2.destroyAllWindows()  #destroy any leftover windows from previous sessions.
#logging config
                              
logging.basicConfig(
    filename="logs/debug.log",
    filemode="w",
    format='%(asctime)s - %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO)

#could set a "last action to move back if no new aciton is found."
actions = {
    "enterInn": False,
}

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

#No cooldown time
pyautogui.PAUSE = 0
class Bot: 
    def __init__(self):
        self.run = True

class Image:
  def __init__(self, imagePath):
    self.image = cv2.imread(imagePath)
    self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
    self.w, self.h = self.image_gray.shape[::-1]
    self.loot_index = 1

screenReader = ScreenReader()


#turn these to objects. 
#template and dimensions
image_enemyHealthBar = Image("imgs/enemyHealthBar.png")

# game window dimensions
x, y, w, h = 5, 30, 1920, 1083

#wait
sleep(2)


while True:

    screenReader.getCurrentScreen()
    screenReader.findImageMatch(image_enemyHealthBar)

    # for key in actions:
    #     # logMsg(key + " : " + str(actions[key]))

    #     if not actions[key]:
    #         if key is "enterInn":
    #             findLocationToClick(match_inn, image_gray, screen, key)

    #         break

cv2.destroyAllWindows()




