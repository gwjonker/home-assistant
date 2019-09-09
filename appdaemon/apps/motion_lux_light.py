import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime

class MotionLuxLight(hass.Hass):

    def initialize(self):
        if "motion_entity" in self.args:
            self.listen_state(self.motion, self.args["motion_entity"])
        else:
            self.log("No motion_entity specified, doing nothing")
    
    def motion(self, entity, attribute, old, new, kwargs):
        self.log("Change detected for {}: from {} to {}".format(self.args["motion_entity"], old,new))
        
        if new == "on" or new== "off":
            curr_time = datetime.now()
            start = self.todayAt(self.args["sleeping"]["start"])
            end = self.todayAt(self.args["sleeping"]["end"])
            curr_lux = self.get_state(self.args["lux_entity"])

            if self.isSleepingTime(curr_time,start,end):
                self.log("Time {} is within start {} and end {}".format(curr_time,start,end))

                lux_below = self.args["periods"]["sleeping"]["lux_below"]
                if float(curr_lux) < float(lux_below):
                    self.log("Current light {} lower then {}".format(curr_lux,lux_below))

                    i = 0
                    for interval in self.args["periods"]["sleeping"]["intervals"]:
                        duration = self.args["periods"]["sleeping"]["intervals"][(interval)]["duration"]
                        brightness = self.args["periods"]["sleeping"]["intervals"][(interval)]["brightness"]
                
                        if i == 0:
                            wait = 0
                            self.run_in(self.setBrightness(self.args["light_entity"],brightness),wait,**kwargs)
                            self.log("Interval {} (no {}) duration {} brightness {} wait {}".format(interval,i,duration,brightness, wait))
                            wait = wait + duration
                        else:
                             self.run_in(self.setBrightness(self.args["light_entity"],brightness),wait,**kwargs)
                             self.log("Interval {} (no {}) duration {} brightness {} wait {}".format(interval,i,duration,brightness, wait))
                             wait = wait + duration
                        i = i + 1

                    self.run_in(self.light_off(self.args["light_entity"]),wait,**kwargs)


    def setBrightness(self,entity,brightness):
        self.set_state(entity, state ="on", attributes = {"brightness": brightness})
        self.log("Brightness of {} set to {}".format(entity,brightness))


    def light_off(self,entity):
        self.turn_off(entity)
        self.log("Turned off entity {}".format(entity))


    def isSleepingTime(self,time,time_start,time_end):
        if time >= time_start or time <= time_end:
            return True
        else:
            return False
    
    def todayAt(self,str_time):
        hr,min,sec = str_time.split(":")
        now = datetime.now()
        return now.replace(hour=int(hr), minute=int(min), second=int(sec), microsecond=0)

    
