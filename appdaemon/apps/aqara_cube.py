import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime


class CubeControl(hass.Hass):

    def initialize(self):
        if 'event' in self.args:
            self.listen_event(self.handle_event, self.args['event'])

    def handle_event(self, event_name, data, kwargs):
        event_data = data["event"]
        event_id = data["id"]
        event_received = datetime.now()
        if data['id'] == self.args['id']:
            self.log(data['event'])
            if data['event'] in [1000, 2000, 3000, 4000, 5000, 6000]:
                self.set_state("sensor.aqara_cube", state='slide', attributes={
                               "event_data": event_data, "event_received": str(event_received)})
            elif data['event'] in [1001, 2002, 3003, 4004, 5005, 6006]:
                self.set_state("sensor.aqara_cube", state='double tap', attributes={
                               "event_data": event_data, "event_received": str(event_received)})
            elif data['event'] in [1006, 2005, 3004, 4003, 5002, 6001]:
                self.set_state("sensor.aqara_cube", state='flip180', attributes={
                               "event_data": event_data, "event_received": str(event_received)})
            elif data['event'] in [1002, 1003, 1004, 1005, 2001, 2003, 2004, 2006, 3001, 3002, 3005, 3006, 4001, 4002, 4005, 4006, 5001, 5003, 5004, 5006, 6002, 6003, 6004, 6005]:
                self.set_state("sensor.aqara_cube", state='flip90', attributes={
                               "event_data": event_data, "event_received": str(event_received)})
            elif data['event'] == 7007:
                self.set_state("sensor.aqara_cube", state='shake', attributes={
                               "event_data": event_data, "event_received": str(event_received)})
            elif data['event'] == 7008:
                self.set_state("sensor.aqara_cube", state='fall', attributes={
                               "event_data": event_data, "event_received": str(event_received)})
            elif data['event'] == 7000:
                self.set_state("sensor.aqara_cube", state='wake', attributes={
                               "event_data": event_data, "event_received": str(event_received)})
            elif len(str(event_data)) != 4 or str(event_data)[1:3] != '00':
                if data['event'] > 0:
                    self.set_state("sensor.aqara_cube", state='rotate cw', attributes={
                                   "event_data": event_data, "event_received": str(event_received)})
                elif data['event'] < 0:
                    self.set_state("sensor.aqara_cube", state='rotate ccw', attributes={"event_data": event_data, "event_received": str(event_received)})'''
