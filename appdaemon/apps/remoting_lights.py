import appdaemon.plugins.hass.hassapi as hass

class TurnOffLight(hass.Hass):

    def initialize(self):
        self.listen_state(self.turn_off_lights, "sensor.mi_magic_cube", new = "shake")

    def turn_off_lights(self, entity, attribute, old, new, kwargs):
        for light in self.args["lights"]:
            self.turn_off(light)
            self.log("Turned off light: {}".format(light))


class TurnOnLight(hass.Hass):

    def initialize(self):
        self.listen_state(self.turn_on_lights, "sensor.mi_magic_cube", new = "flip90")

    def turn_on_lights(self, entity, attribute, old, new, kwargs):
        for light in self.args["lights"]:
            self.turn_on(light)
            self.log("Turned on light: {}".format(light))
