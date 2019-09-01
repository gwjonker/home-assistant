import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime

class DeconzHelper(hass.Hass):
    def initialize(self) -> None:
        self.listen_event(self.event_received, "deconz_event")


    def event_received(self, event_name, data, kwargs):
        event_data = data["event"]
        event_id = data["id"]
        event_received = datetime.now()

        self.log("Deconz event received from {}. Event was: {}".format(event_id, event_data))

        if event_data in [1000, 2000, 3000, 4000, 5000, 6000]:
            self.set_state("sensor.mi_magic_cube_event", state = 'slide', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
            mod_brightness = -75

        elif event_data in [1001, 2002, 3003, 4004, 5005, 6006]:
            self.set_state("sensor.mi_magic_cube_event", state = 'double tap', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
            mod_brightness = 25

        elif event_data in [1006, 2005, 3004, 4003, 5002, 6001]:
            self.set_state("sensor.mi_magic_cube_event", state = 'flip180', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
            mod_brightness = 25

        elif event_data in [1002, 1003, 1004, 1005, 2001, 2003, 2004, 2006, 3001, 3002, 3005, 3006, 4001, 4002, 4005, 4006, 5001, 5003, 5004, 5006, 6002, 6003, 6004, 6005]:
            self.set_state("sensor.mi_magic_cube_event", state = 'flip90', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
            mod_brightness = 50

        elif event_data == 7007:
            self.set_state("sensor.mi_magic_cube_event", state = 'shake', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
            mod_brightness = 0
        
        elif event_data == 7008:
            self.set_state("sensor.mi_magic_cube_event", state = 'fall', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
        elif event_data == 7000:
            self.set_state("sensor.mi_magic_cube_event", state = 'wake', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
        elif len(str(event_data)) != 4 or str(event_data)[1:3] != '00':
                if event_data > 0:
                    self.set_state("sensor.mi_magic_cube_event", state = 'rotate cw', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})
                elif event_data < 0:                                 
                    self.set_state("sensor.mi_magic_cube_event", state = 'rotate ccw', attributes = {"event_data": event_data, "event_id": event_id, "event_received": str(event_received)})


        def NewValidBrightness(cur, mod):
            if mod == 0:
                new = 0
            elif mod != 0:
                new = cur + mod
                if new >= 254:
                    new = new - 254
                elif new <= 0:
                    new = 0
            return new;

        #Woonkamer linksvoor
        cur_brightness = self.get_state("light.woonkamer_linksvoor_level", attribute ="brightness") or 0
                
        new_brightness = NewValidBrightness(cur = cur_brightness, mod = mod_brightness)
        
        if new_brightness == 0:
            self.turn_off("light.woonkamer_linksvoor_level")
            self.log("entities.light.woonkamer_linksvoor_level.attributes.brightness is off")
        elif new_brightness > 0:
            self.turn_on("light.woonkamer_linksvoor_level", brightness = new_brightness)
            self.log("entities.light.woonkamer_linksvoor_level.attributes.brightness is {}".format(new_brightness))

        #Woonkamer rechtsvoor
        cur_brightness = self.get_state("light.woonkamer_rechtsvoor_level", attribute ="brightness") or 0
                
        new_brightness = NewValidBrightness(cur = cur_brightness, mod = mod_brightness)
        
        if new_brightness == 0:
            self.turn_off("light.woonkamer_rechtsvoor_level")
            self.log("entities.light.woonkamer_rechtsvoor_level.attributes.brightness is off")
        elif new_brightness > 0:
            self.turn_on("light.woonkamer_rechtsvoor_level", brightness = new_brightness)
            self.log("entities.light.woonkamer_rechtsvoor_level.attributes.brightness is {}".format(new_brightness))
    


        