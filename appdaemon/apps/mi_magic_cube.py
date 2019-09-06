import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime

class MiMagicCube(hass.Hass):
    def initialize(self):
        self.listen_event(self.event_received, "deconz_event")


    def event_received(self, event_name, data, kwargs):
        event_data = data["event"]
        entity = data["id"]
        timestamp = datetime.now()


        if entity == "mi_magic_cube":
            self.log("Deconz event received from {}. Event was: {}".format(entity, event_data))

            if event_data in [1000, 2000, 3000, 4000, 5000, 6000]:
                self.set_state("sensor.mi_magic_cube", state = 'slide', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})

            elif event_data in [1001, 2002, 3003, 4004, 5005, 6006]:
                self.set_state("sensor.mi_magic_cube", state = 'double tap', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})

            elif event_data in [1006, 2005, 3004, 4003, 5002, 6001]:
                self.set_state("sensor.mi_magic_cube", state = 'flip180', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})

            elif event_data in [1002, 1003, 1004, 1005, 2001, 2003, 2004, 2006, 3001, 3002, 3005, 3006, 4001, 4002, 4005, 4006, 5001, 5003, 5004, 5006, 6002, 6003, 6004, 6005]:
                self.set_state("sensor.mi_magic_cube", state = 'flip90', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})

            elif event_data == 7007:
                self.set_state("sensor.mi_magic_cube", state = 'shake', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})
            
            elif event_data == 7008:
                self.set_state("sensor.mi_magic_cube", state = 'fall', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})
           
            elif event_data == 7000:
                self.set_state("sensor.mi_magic_cube", state = 'wake', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})
           
            elif len(str(event_data)) != 4 or str(event_data)[1:3] != '00':
                    if event_data > 0:
                        self.set_state("sensor.mi_magic_cube", state = 'rotate cw', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})
                    elif event_data < 0:                                 
                        self.set_state("sensor.mi_magic_cube", state = 'rotate ccw', attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})

            self.log("Sensor.mi_magic_cube set to {}".format(self.get_state("sensor.mi_magic_cube")))
    


        