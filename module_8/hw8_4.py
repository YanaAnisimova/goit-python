import math


def cil_volume(h, r, x):

    return h * math.sin(math.radians(x)) * math.pi * r**2


cil_volume(h, r, x)
