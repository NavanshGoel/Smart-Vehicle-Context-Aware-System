class WindowGlass:
    def __init__(self):
        self.movement = "CLOSED"
        self.hault = True

    def setWindow(self, statusMove):
        if statusMove not in ("OPEN","CLOSED","OPENING", "CLOSING"):
            print("Error! Enter valid option from (OPEN/CLOSED/OPENING/CLOSING)")
        else:
            self.movement = statusMove

class WindowFrame:
    def __init__(self):
        self.obstacle = False
        
    def windowObstacle(self,statusobstacle):
        if statusobstacle not in (True,False):
            print("Error! Enter valid option from (true, false)")
        else:
            self.obstacle = statusobstacle

class autoObstacleDetection(WindowGlass, WindowFrame):
    def __init__(self):
        WindowGlass.__init__(self)
        WindowFrame.__init__(self)

    def printStatus(self):
        print("---**STATUS**---\nWindow Status: {}\nWindow Hault: {}\nObstacle: {}\n---**END**---\n".format(self.movement,self.hault, self.obstacle))

class TimeStamp:
    def __init__(self,ir, openWindow, closeWindow):
        self.ir = ir
        self.openWindow = openWindow
        self.closeWindow = closeWindow

    def printTimeStamp(self):
        print("IR Sensor: {} | Open Window: {} | Close Window: {}".format(self.ir,self.openWindow,self.closeWindow))  

class GlobalTimeStamp:
    def __init__(self,time, temp, flow, humidity, sunSensor, rainSensor, ir, openWindow, closeWindow):
        self.time = time
        self.temp = temp
        self.flow = flow
        self.humidity = humidity
        self.sunSensor = sunSensor
        self.rainSensor = rainSensor
        self.ir = ir
        self.openWindow = openWindow
        self.closeWindow = closeWindow
        
def checkBehaviour4(cntrlSystem, timestamp):
    prevMov,prevHault, prevObst = cntrlSystem.movement,cntrlSystem.hault, cntrlSystem.obstacle
    # No obstacle detected
    if timestamp.ir == 0:
        cntrlSystem.windowObstacle(False)
        if timestamp.openWindow == 1 and timestamp.closeWindow == 1:
            # if both and close window command simultaneously
            print("Invalid Input\n")
        elif timestamp.openWindow == 1:
            # open window command
            if prevMov == "OPENING" or prevMov == "OPEN":
                cntrlSystem.setWindow("OPEN")
            else:
                cntrlSystem.hault = False
                cntrlSystem.setWindow("OPENING")
        elif timestamp.closeWindow == 1:
            # close window command
            if prevMov == "CLOSING" or prevMov == "CLOSED":
                cntrlSystem.hault = True
                cntrlSystem.setWindow("CLOSED")
            else:
                cntrlSystem.hault = False
                cntrlSystem.setWindow("CLOSING")
        elif prevMov == "OPENING":
            # if was previously in opening condition 
            cntrlSystem.setWindow("OPEN")
        elif prevMov == "CLOSING":
            # if was previously in closing condition and no obstacle detected set to closed
            cntrlSystem.hault=True
            cntrlSystem.setWindow("CLOSED")
        else:
            # if prevously obstacle was detected
            print("Resumed Window - {}\n".format(prevMov))
            cntrlSystem.hault=True
            cntrlSystem.hault = False
            if prevMov == "OPENING":
                # resume opening
                cntrlSystem.setWindow("OPEN")
            elif prevMov == "CLOSING":
                # resume closing
                cntrlSystem.setWindow("CLOSED")
    else:
        # Obstacle is detected
        cntrlSystem.windowObstacle(True)
        if timestamp.openWindow == 1 and timestamp.closeWindow == 1:
            # if both and close window command simultaneously
            cntrlSystem.hault=True
            print("Invalid Input\n")
        elif timestamp.openWindow == 1:
            # open window command with obstacle
            cntrlSystem.setWindow("OPENING")
            if prevMov == "OPENING":
                cntrlSystem.setWindow("OPEN")
        elif prevMov == "OPENING":
            # if was previously in opening condition 
            cntrlSystem.setWindow = "OPEN"
        elif timestamp.closeWindow == 1 and prevMov != "CLOSED":
            # close window command with obstacle
            cntrlSystem.hault=True
            cntrlSystem.setWindow("CLOSING")
        elif timestamp.openWindow == 0 or timestamp.closeWindow == 0:
            
            if prevMov == "CLOSING":
                # an initial closing command with a current obstacle
                cntrlSystem.setWindow("CLOSING")
                cntrlSystem.hault=True
        else:
            # obstacle detected but window already opened or closed
            print("No effect of obstacle as window : {}".format(prevMov))
    # print("{}, {}, {}\n".format(cntrlSystem.movement,cntrlSystem.hault, cntrlSystem.obstacle))
    if prevMov == cntrlSystem.movement and prevHault == cntrlSystem.hault and prevObst == cntrlSystem.obstacle:
        return False
    else:
        return True

      

def main():
    globalDataSet = []
    
    globalDataSet.append(GlobalTimeStamp(1,30.00,40.0, 40,0,0.7,0,1,0))
    globalDataSet.append(GlobalTimeStamp(2,35.00,33.78,50,100,0.4,1,1,0))
    globalDataSet.append(GlobalTimeStamp(3,34.25,-46.2,46,800,0.0,1,0,1))
    globalDataSet.append(GlobalTimeStamp(4,37.00,50.4,60,1600,0.0,1,0,0))
    globalDataSet.append(GlobalTimeStamp(5,40.00,4.7,63,0,1.5,0,0,1))
    globalDataSet.append(GlobalTimeStamp(6,35.50,28.32,40,0,4.5,1,0,1))
    globalDataSet.append(GlobalTimeStamp(7,42.00,-15.0,70,400,0.2,0,0,1))
    
    
    dataSet = []
    
    for t in globalDataSet:
        dataSet.append(TimeStamp(t.ir, t.openWindow, t.closeWindow))

    a = autoObstacleDetection()

    contextList = []
    
    for timestamp in dataSet:
        timestamp.printTimeStamp()
        a.printStatus()
        print("Checking Behavior 4")
        if checkBehaviour4(a,timestamp):
            a.printStatus()
            contextList.append(a)

if __name__ == "__main__":
    main()



