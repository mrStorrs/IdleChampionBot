import cv2
import pyautogui
import numpy as np
from time import sleep

x, y, w, h = 0, 0, 1280, 752

class ScreenReader:    
    def getCurrentScreen(self):
        #take a screen shot then convert it to cv2 readable form.
        
        self.screen = cv2.cvtColor(
            np.array(pyautogui.screenshot(region=(x, y, w, h))),
            cv2.COLOR_RGB2BGR
        )
        #save the image in grey for matching l8r
        self.image_gray = cv2.cvtColor(self.screen, cv2.COLOR_RGB2GRAY)
        #if q is pressed while the mini-image is the active window. Close everything.
        if cv2.waitKey(1) == ord('q'):
            self.close = True

        #show what the computer sees on a mini image screen.
        image_mini = cv2.resize(
            src = self.screen,
            # dsize = (450,350) #must be integer, not float
            dsize = (800,600) #must be integer, not float
        )
        cv2.imshow("vision", image_mini)
        # cv2.waitKey(10)
    
    def findImageMatch(self, imageToFind):
        result = cv2.matchTemplate(
            self.image_gray,
            imageToFind.image_gray,
            cv2.TM_CCOEFF_NORMED
        )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)



        #threshold
        if max_val >= 0.80:
            pyautogui.click(
                x = max_loc[0] + x, #screen x
                y = max_loc[1] + y  #screen y
            )
            pyautogui.click(
                x = max_loc[0] + x, #screen x
                y = max_loc[1] + y  #screen y
            )

            #highlight found objects
            # w, h = imageToFind.image_gray.shape[::-1] #used for bounding boxes
            self.screen = cv2.rectangle(
                img = self.screen,
                pt1 = max_loc,
                pt2 = (
                    max_loc[0] + imageToFind.w, # = pt2 x 
                    max_loc[1] + imageToFind.h # = pt2 y
                ),
                color = (0,0,255),
                thickness = 1 #fill the rectangle
            )

            image_mini = cv2.resize(
                src = self.screen,
                # dsize = (450,350) #must be integer, not float
                dsize = (800,600) #must be integer, not float
            )
            cv2.imshow("vision", image_mini)
