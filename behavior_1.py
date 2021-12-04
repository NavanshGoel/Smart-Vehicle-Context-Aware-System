class AC:
    def __init__(self):
        self.flow = "na"
        self.statusAC = "OFF"

    def setFlow(self, flow):
        if flow not in ("low","medium","high","na"):
            print("Error! Enter valid option from (low/medium/high/na)")
        else:
            self.flow = flow

    def setACStatus(self, statusAC):
        if statusAC not in ("ON","OFF"):
            print("Error! Enter valid option from (ON/OFF)")
        else:
            self.statusAC = statusAC
        
class ventDuct:
    def __init__(self):
        self.power = "na"
        self.statusVD = "OFF"

    def setPower(self, power):
        if power not in ("low","medium","high","na"):
            print("Error! Enter valid option from (low/medium/high/na)")
        else:
            self.power = power

    def setVDStatus(self, statusVD):
        if statusVD not in ("ON","OFF"):
            print("Error! Enter valid option from (ON/OFF)")
        else:
            self.statusVD = statusVD

class People:
    def __init__(self):
        self.number = 0

    def setPeople(self, people):
        self.number = people

    def increasePeople(self):
        self.number = self.number + 1
    
    def decreasePeople(self):
        if self.number>0:
            self.number = self.number - 1
        else:
            print("Error! number of people already zero, object crossed is not a person")

class autoTempControl(AC, ventDuct, People):
    def __init__(self):
        AC.__init__(self)
        ventDuct.__init__(self)
        People.__init__(self)

    def printStatus(self):
        print("---**STATUS**---\nAC Status: {}\nAC Flow: {}\nVentilation Duct Status: {}\nVentilation Duct Power: {}\nNumber of People: {}\n---**END**---\n".format(self.statusAC, self.flow, self.statusVD, self.power, self.number))

class TimeStamp:
    def __init__(self, temp, flow, humidity):
        self.temp = temp
        self.flow = flow
        self.humidity = humidity

    def printTimeStamp(self):
        print("Temperature: {} | Flow Sensor Output: {} | Humidity: {}".format(self.temp,self.flow,self.humidity))  


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
        
def checkBehaviour1(cntrlSystem, timestamp):
    prevNum, prevFlow, prevPower = cntrlSystem.number, cntrlSystem.flow, cntrlSystem.power
    
    #Hardware Failure
    if timestamp.flow == "NA" or timestamp.temp == "NA" or timestamp.humidity == "NA":
        print("Sensor Error.... Repair Sensor.....\n")
    
    if timestamp.flow>0:
        cntrlSystem.setPeople(cntrlSystem.number+1)
    elif timestamp.flow<0:
        cntrlSystem.setPeople(cntrlSystem.number-1)

    if cntrlSystem.number == 0:
        ventDuct.__init__()
        AC.__init__()
        
    if cntrlSystem.number>=prevNum:
        #change the temp
        if cntrlSystem.statusAC != "ON":
            cntrlSystem.setACStatus("ON")
        if timestamp.temp > 40:
            cntrlSystem.setFlow("high")
        elif timestamp.temp > 30 and timestamp.temp < 40:
            cntrlSystem.setFlow("medium")
        else:
            cntrlSystem.setFlow("low")
        #change the ventilation settings
        if cntrlSystem.statusVD != "ON":
            cntrlSystem.setVDStatus("ON")
        if timestamp.humidity > 60:
            cntrlSystem.setPower("high")
        elif timestamp.humidity <= 40 and timestamp.humidity > 30:
            cntrlSystem.setPower("medium")
        else:
            cntrlSystem.setPower("low")  
    else:
        if cntrlSystem.statusAC != "ON":
            cntrlSystem.setACStatus("ON")  
        if cntrlSystem.statusVD != "ON":
            cntrlSystem.setVDStatus("ON")
        #decrease AC flow
        if prevFlow == "high":
            cntrlSystem.flow = "medium"
        elif prevFlow == "medium":
            cntrlSystem.flow = "low"
        #decrease ventilation power
        if prevPower == "high":
            cntrlSystem.power = "medium"
        elif prevPower == "medium":
            cntrlSystem.power = "low"

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
        dataSet.append(TimeStamp(t.temp, t.flow, t.humidity))

    a = autoTempControl()

    contextList = []

    for timestamp in dataSet:
        timestamp.printTimeStamp()
        a.printStatus()
        print("Checking Behavior 1")
        checkBehaviour1(a,timestamp)
        a.printStatus()
        contextList.append(a)

if __name__ == "__main__":
    main()

