__author__ = 'Ricardo'

from ifes.util.State import State

class StateNormal(State):
    def __init__(self, helicoptero):
        State.helicoptero = helicoptero
    def set_forca(self):
        State.helicoptero.tiros += 50
