import pandas as pd

class Weather:
    def __init__(self):
        self.rainStatus = False
        self.sunStatus = False
        self.sunIntensity = 0
        self.rainIntensity = 0
    
    def setRainStatus(self, status):
        if status not in (True,False):
            print("Error! Enter valid option from (True, False)")
        else:
            self.rainStatus = status
            
    def setSunStatus(self, status):
        if status not in (True,False):
            print("Error! Enter valid option from (True, False)")
        else:
            self.sunStatus = status

    def setRainIntensity(self, intensity):
        if intensity not in (0,1,2,3):
            print("Error! Enter valid option from (0,1,2,3)")
        else:
            self.rainIntensity = intensity
            print(intensity)
            
    def setSunIntensity(self, sIntensity):
        if sIntensity not in (0,1,2,3):
            print("Error! Enter valid option from (0,1,2,3)")
        else:
            self.sunIntensity = sIntensity

class Wipers:
    def __init__(self):
        self.wiperStatus = False
        self.wiperSpeed = 0
        
    def setWiperStatus(self, status):
        if status not in (True,False):
            print("Error! Enter valid option from (True, False)")
        else:
            self.wiperStatus = status

    def setWiperSpeed(self, speed):
        if speed not in (0,1,2,3):
            print("Error! Enter valid option from (0,1,2,3)")
        else:
            self.wiperSpeed = speed
    
class Sunroof:
    def __init__(self):
        self.sunroofStatus = False
        
    def setSunroofStatus(self, status):
        if status not in (True,False):
            print("Error! Enter valid option from (True, False)")
        else:
            self.sunroofStatus = status
    
class SunShades:
    def __init__(self):
        self.sunshadeStatus = False
        
    def setSunshadeStatus(self, statusShades):
        if statusShades not in (True, False):
            print("Error! Enter valid option from (True, False)")
        else:
            self.sunshadeStatus = statusShades  
     
class Monitor:
    def __init__(self):
        self.notification = "NA"
    
    def setNotification(self, note):
        self.notification = note
        print(self.notification)
        
    def defaultNotification(self):
        self.notification = "NA"
   
        
class autoWeatherControl(Wipers, Sunroof, SunShades, Monitor, Weather):
    def __init__(self):
        Wipers.__init__(self)
        Sunroof.__init__(self)
        SunShades.__init__(self)
        Monitor.__init__(self)
        Weather.__init__(self)

    def printStatus(self):
        print("---**STATUS**---\nSun Status: {}\nSun Intensity: {}\nRain Status: {}\nRain Intensity: {}\nWiper Status: {}\nWiper Speed: {}\nSunroof Status: {}\nSun Shade Status: {}\nMonitor Notification: {}\n---**END**---\n".format(self.sunStatus, self.sunIntensity, self.rainStatus, self.rainIntensity, self.wiperStatus, self.wiperSpeed, self.sunroofStatus, self.sunshadeStatus, self.notification))

class TimeStamp:
    def __init__(self, sunSensor, rainSensor):
        self.rainSensor = rainSensor
        self.sunSensor = sunSensor

    def printTimeStamp(self):
        print("Rain Sensor Value: {} | Sunrays Sensor: {}".format(self.rainSensor,self.sunSensor))  

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
        
        
def checkBehaviour2(cntrlsystem, timestamp):
    # cntrlsystem.defaultNotification()
    
    #Hardware Failure
    if timestamp.sunSensor == "NA" or timestamp.rainSensor == "NA":
        print("Sensor Error.... Repair Sensor.....\n")
    
    if timestamp.sunSensor <= 0:
        cntrlsystem.setSunStatus(False)
        cntrlsystem.setSunIntensity(0)
    else:
        if cntrlsystem.sunStatus != True:
            cntrlsystem.setSunStatus(True)
        
        if timestamp.sunSensor < 750:
            cntrlsystem.setSunIntensity(1)
        elif timestamp.sunSensor >= 750 and timestamp.sunSensor < 1500 :
            cntrlsystem.setSunIntensity(2)
        else:
            cntrlsystem.setSunIntensity(3)
            
    if timestamp.rainSensor < 0.3:
        cntrlsystem.setRainStatus = False
        cntrlsystem.setRainIntensity = 0
    else:
        if cntrlsystem.rainStatus != True:
            cntrlsystem.setRainStatus(True)
        
        if timestamp.rainSensor < 1.5:
            cntrlsystem.setRainIntensity(1)
        elif timestamp.rainSensor >= 1.5 and timestamp.rainSensor < 3.0 :
            cntrlsystem.setRainIntensity(2)
        elif timestamp.rainSensor >= 3.0:
            cntrlsystem.setRainIntensity(3)
    
    #wiper and sunroof control
    if cntrlsystem.rainStatus:
        cntrlsystem.setWiperStatus(True)
        cntrlsystem.setSunroofStatus(False)
        #set wiper speed
        if cntrlsystem.rainIntensity == 1:
            cntrlsystem.setWiperSpeed(1)
        elif cntrlsystem.rainIntensity == 2:
            cntrlsystem.setWiperSpeed(2)
        else:
            cntrlsystem.setWiperSpeed(3)
    else:
        if cntrlsystem.wiperStatus or cntrlsystem.wiperSpeed > 0:
            cntrlsystem.setWiperStatus(False)
            cntrlsystem.setWiperSpeed(0)
        
        if cntrlsystem.sunIntensity==3 and cntrlsystem.sunStatus:
            cntrlsystem.setSunroofStatus(False)
        else:
            #give passive option to open sunroof
            cntrlsystem.setNotification("Open Sunroof?\n")
            input_val = input("Y/N: ")
            if (input_val in ["Y", "y", "yes", "YES"]) and cntrlsystem.sunroofStatus == False:
                cntrlsystem.setSunroofStatus(True)
            else:
                cntrlsystem.setSunroofStatus(False)
    
def checkBehaviour3(cntrlsystem, timestamp):
    if timestamp.sunSensor <= 0:
        cntrlsystem.setSunStatus(False)
        cntrlsystem.setSunIntensity(0)
    else:
        if cntrlsystem.sunStatus != True:
                cntrlsystem.setSunStatus(True)
        if timestamp.sunSensor < 750:
            cntrlsystem.setSunIntensity(1)
        elif timestamp.sunSensor >= 750 and timestamp.sunSensor < 1500 :
            cntrlsystem.setSunIntensity(2)
        else:
            cntrlsystem.setSunIntensity(3)
    
    if cntrlsystem.sunIntensity==3 and cntrlsystem.sunStatus and cntrlsystem.sunshadeStatus:
        #give passive option to close sunshade
        cntrlsystem.setNotification("Close Sunshade?\n")
        input_val = input("Y/N: ")
        if (input_val in ["Y", "y", "yes", "YES"]) and cntrlsystem.sunshadeStatus == False:
            cntrlsystem.setSunshadeStatus(False)
        else:
            cntrlsystem.setSunshadeStatus(True)   
    else:
        #give passive option to open sunshade
        if not cntrlsystem.sunshadeStatus:
            cntrlsystem.setNotification("Open Sunshade?\n")
            input_val = input("Y/N: ")
            if (input_val in ["Y", "y", "yes", "YES"]) and cntrlsystem.sunshadeStatus == False:
                cntrlsystem.setSunshadeStatus(True)
            else:
                cntrlsystem.setSunshadeStatus(False)

def main():
    globalDataSet = []
    
    df = pd.read_csv("dataset.csv")
    globalDataSet.append(GlobalTimeStamp(1, 30.00, 40.0, 40, 0, 0.7, 0, 1, 0))
    globalDataSet.append(GlobalTimeStamp(2, 35.00, 33.78, 50, 100, 0.4, 1, 1, 0))
    globalDataSet.append(GlobalTimeStamp(3, 34.25, -46.2, 46, 800, 0.0, 1, 0, 1))
    globalDataSet.append(GlobalTimeStamp(4, 37.00, 50.4, 60, 1600, 0.0, 1, 0, 0))
    globalDataSet.append(GlobalTimeStamp(5, 40.00, 4.7, 63, 0, 1.5, 0, 0, 1))
    globalDataSet.append(GlobalTimeStamp(6, 35.50, 28.32, 40, 0, 4.5, 1, 0, 1))
    globalDataSet.append(GlobalTimeStamp(7, 42.00, -15.0, 70, 400, 0.2, 0, 0, 1))
    
    
    dataSet = []
    
    for t in globalDataSet:
        dataSet.append(TimeStamp(t.sunSensor, t.rainSensor))

    a = autoWeatherControl()

    contextList = []

    for timestamp in dataSet:
        timestamp.printTimeStamp()
        a.printStatus()
        print("Checking Behavior 2")
        checkBehaviour2(a,timestamp)
        a.printStatus()
        print("Checking Behavior 3")
        checkBehaviour3(a,timestamp)
        a.printStatus()
        contextList.append(a)
    
if __name__=="__main__":
    main()