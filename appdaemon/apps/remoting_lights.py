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
        self.listen_state(self.turn_on_lights, "sensor.mi_magic_cube", new = "slide")

    def turn_on_lights(self, entity, attribute, old, new, kwargs):
        for light in self.args["lights"]:
            self.turn_on(light)
            self.log("Turned on light: {}".format(light))


class IncreaseBrightnessLight(hass.Hass):

    def initialize(self):
        self.listen_state(self.inc_brightness_lights, "sensor.mi_magic_cube", new = "flip90")

    def inc_brightness_lights(self, entity, attribute, old, new, kwargs):
        step = self.args["step"]
        for light in self.args["lights"]:
            if self.get_state(light) == "on":
                cb = self.get_state(light, attribute = "brightness")
                
                nb = cb + step
                if (nb)>253:
                    nb = 254
                
                self.set_state(light, attributes = { "brightness": nb})
                self.log("brightness light {} is set from brightness {} to {}".format(light, cb, nb))


class DecreaseBrightnessLight(hass.Hass):

    def initialize(self):
        self.listen_state(self.dec_brightness_lights, "sensor.mi_magic_cube", new = "flip180")

    def dec_brightness_lights(self, entity, attribute, old, new, kwargs):
        step = self.args["step"]
        for light in self.args["lights"]:
            if self.get_state(light) == "on":
                cb = self.get_state(light, attribute = "brightness")
                
                nb = cb - step
                if (nb)<1:
                    nb = 0
                
                self.set_state(light, attributes = { "brightness": nb})
                self.log("brightness light {} is set from brightness {} to {}".format(light, cb, nb))

