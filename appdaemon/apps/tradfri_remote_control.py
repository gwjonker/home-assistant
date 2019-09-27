import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime

class TradfriRemoteControl(hass.Hass):
    def initialize(self):
        self.listen_event(self.event_received, "deconz_event")

    def event_received(self, event_name, data, kwargs):
        event_data = data["event"]
        entity = data["id"]

        if entity == "tradfri_remote_control":
            self.log("Deconz event received from {}. Event was: {}".format(entity, event_data))

            if event_data in [1002]:
                self.setState("toggle",event_data,entity)

            elif event_data in [2002]:
                self.setState("up",event_data,entity)

            elif event_data in [3002]:
                self.setState("down",event_data,entity)

            elif event_data in [4002]:
                self.setState("previous",event_data,entity)

            elif event_data in [5002]:
                self.setState("next",event_data,entity)


    def setState(self,state,event_data,entity):
        timestamp = datetime.now()
        entity = "sensor." + entity
        self.set_state(entity, state = state, attributes = {"event_data": event_data, "entity": entity, "timestamp": str(timestamp)})
        self.log("{} set to {}".format(entity,self.get_state(entity)))
