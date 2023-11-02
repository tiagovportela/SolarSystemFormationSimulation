import random
from simulation import constants

#random color genetator
def random_color():
    return (
        random.randint(0,255), 
        random.randint(0,255), 
        random.randint(0,255)
        )

# units converter to pixels
def units_converter(value):
    return value * constants.Units.SCALE_FACTOR     

