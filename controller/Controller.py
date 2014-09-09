from devices.Time import *

class Controller:
    
    def __init__(self):
        self.startRecord = -1
        self.endRecord = -1
        self.timer = Time()
    
    def updateAll(self,canvas,mcp3208,serial,controller,rpm,speed,oilTemp,oilPressure,h2o,h2oEcu,battery,fuel,throttle,clutch,brake,runTime):
        rpm.setRpm(serial.getRpm())
        speed.setText(serial.getVss())
        oilTemp.setValue(mcp3208.getADC(7)) 
        oilPressure.setValue(mcp3208.getADC(6))
        fuel.setWidth(mcp3208.getADC(7))
        h2o.setValue(mcp3208.getADC(5))
        h2oEcu.setValue(int(serial.getEct()))
        battery.setValue(round(serial.getBattery(),1))
        throttle.setHeight(mcp3208.getADC(8))
        clutch.setHeight(mcp3208.getADC(4))
        brake.setHeight(mcp3208.getADC(3))
        time = self.timer.getTime()
        runTime.setText(self.timer.getTimeString())
        canvas.after(10,controller.updateAll,canvas,mcp3208,serial,controller,rpm,speed,oilTemp,oilPressure,h2o,h2oEcu,battery,fuel,throttle,clutch,brake,runTime)

    def checkSpeedRecord(self,speed):
        now = self.timer.getTime()
        if speed <= 0:
            self.startRecord=self.timer.getTime()
        elif (speed >= 100) and (now - self.startRecord < self.endRecord - self.startRecord):
            self.endRecord=now
        
