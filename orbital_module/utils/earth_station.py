from astropy import units as u

class EarthStation:
    """Define earth station"""
    def __init__(self, name):
        self.name = name
    
    def station_define(self, coordinates=[0,0]):
        self.coord = coordinates * u.deg