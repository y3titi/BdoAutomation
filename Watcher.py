import pyautogui
import pyscreeze
import time
from datetime import datetime

class Watcher:
    confidence_percentage=0.95
    timeformat= "%H:%M:%S.%f: "
    sItemfound = "found: "
    offseticon = 10
    offsetbtn = 10
    screeny=1080
    screenx=1920

    def __init__(self):
        print("Watcher constructor")

    def __init__(self, confPercentage):
        self.confidence_percentage=confPercentage    

    def GetPosItem(self, itemPictureFilename, itemregion, WithConf):

        #print("GetPosItem Start")

        #print(itemregion)
        ItemPos = None

        if (WithConf == True):
            ItemPos = pyautogui.locateOnScreen(itemPictureFilename, region=(itemregion[0], itemregion[1], itemregion[2], itemregion[3]), confidence=self.confidence_percentage)
        else:
            ItemPos = pyautogui.locateOnScreen(itemPictureFilename, region=(itemregion[0], itemregion[1], itemregion[2], itemregion[3]))
    
        if (ItemPos != None):
            snow = datetime.now()
            print(snow.strftime(self.timeformat) , self.sItemfound , ItemPos)
            return ItemPos
        else:
            return None
        
    def GetPosItemWithpercentage(self, itemPictureFilename, itemregion, confPercentage):

        #print("GetPosItem Start")

        #print(itemregion)
        ItemPos = None

        try:
          ItemPos = pyautogui.locateOnScreen(itemPictureFilename, region=(itemregion[0], itemregion[1], itemregion[2], itemregion[3]), confidence=confPercentage)
        except pyautogui.ImageNotFoundException:
          print('ImageNotFoundException: image not found')
          ItemPos = None
        
        if (ItemPos != None):
            snow = datetime.now()
            print(snow.strftime(self.timeformat) , self.sItemfound , ItemPos)
            return ItemPos
        else:
            return None

    def getchatimage(self, TopRight,BottomLeft):
        region = (0,0,self.screenx,self.screeny)
        iconlocTopRight = self.GetPosItem(TopRight, region, True)
        iconlocButtomLeft = self.GetPosItem(BottomLeft, region, True)
        offsetLeft=15
        offsetHeight=10

        if ((iconlocTopRight != None) and (iconlocButtomLeft != None)):


            im = pyautogui.screenshot(region=(iconlocButtomLeft[0] + offsetLeft, iconlocTopRight[1] , iconlocTopRight[0]- iconlocButtomLeft[0], (iconlocButtomLeft[1]- iconlocTopRight[1])- offsetHeight))
            im.save(r".\screenshot.png")
            return True
        else:
            return False