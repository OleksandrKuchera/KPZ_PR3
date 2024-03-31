# -*- coding: utf-8 -*-
class Wave:
    def get_name(self):
        pass

class Radio(Wave):
    def get_name(self):
        return "Radio"

class Sound(Wave):
    def get_name(self):
        return "Sound"

class Visible(Wave):
    def get_name(self):
        return "Visible"

class Infrared(Wave):
    def get_name(self):
        return "Infrared"

class Ultraviolet(Wave):
    def get_name(self):
        return "Ultraviolet"

class Gamma(Wave):
    def get_name(self):
        return "Gamma"

class XRay(Wave):
    def get_name(self):
        return "XRay"


class Sense(Sound, Radio):
    pass

class TNT(Sound,Visible,Infrared):
    pass

class Light_Bulb(Infrared, Visible, Ultraviolet):
    pass

class Sun (Infrared,Visible,Ultraviolet,Gamma,XRay):
    pass

lamp = Light_Bulb()
sense = Sense()

print(lamp.get_name())
print(sense.get_name())



