import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

#FUNCTIONS TO CHANGE INDIVIDUAL COLUMNS
def speed_limit(rate):
    speed = float(rate)
    if speed < 10:
        return '-10'
    elif speed < 15:
        return '10'
    elif speed < 20:
        return '15'
    elif speed < 25:
        return '20'
    elif speed < 30:
        return '25'
    elif speed < 35:
        return '30'
    elif speed < 40:
        return '35'
    elif speed < 45:
        return '40'
    elif speed < 50:
        return '45'
    else:
        return '+45'
    
    
def traffic_device(device):
    keep = ['NO CONTROLS', 'TRAFFIC SIGNAL', 'STOP SIGN/FLASHER', 'UNKNOWN', 'OTHER']
    if device in keep:
        return device
    else:
        return 'OTHER'

    
def weather(condition):
    keep = ['CLEAR', 'RAIN', 'SNOW', 'UNKNOWN', 'OTHER']
    if condition in keep:
        return condition
    else:
        return 'OTHER'


def defects(defect):
    keep = ['NO DEFECTS', 'UNKNOWN', 'OTHER']
    if defect in keep:
        return defect
    else:
        return 'OTHER'

    
def time(hour):
    peak = [6,7,8,9,10,14,15,16,17,18,19]
    if hour in peak:
        return 'RUSH HRS'
    else:
        return 'NON RUSH HRS'

    
def age_range(age):
    if age <= 15:
        return 'TOO YOUNG'
    if age < 20:
        return 'TEENAGER'
    elif age < 30:
        return 'TWENTIES'
    elif age < 40:
        return 'THIRTIES'
    elif age < 50:
        return 'FORTIES'
    elif age < 60:
        return 'FIFTIES'
    elif age < 70:
        return 'SIXTIES'
    elif age < 80:
        return 'SEVENTIES'
    else:
        return 'EIGHTY OR OLDER'

    
def safety(equipment):
    keep = ['USAGE UNKNOWN', 'NONE PRESENT']
    used = ['SAFETY BELT USED', 'CHILD RESTRAINT USED', 'CHILD RESTRAINT - FORWARD FACING', 
            'BICYCLE HELMET (PEDACYCLIST INVOLVED ONLY)', 'HELMET USED', 'DOT COMPLIANT MOTORCYCLE HELMET', 
            'CHILD RESTRAINT - TYPE UNKNOWN', 'CHILD RESTRAINT - REAR FACING', 'BOOSTER SEAT']
    if equipment in keep:
        return equipment
    elif equipment in used:
        return 'SAFETY USED'
    elif 'IMPROPERLY' in equipment:
        return 'USED IMPROPERLY'
    elif 'NOT USED' in equipment:
        return 'NOT USED'
    elif 'NOT DOT' in equipment:
        return 'USED IMPROPERLY'
    else:
        return 'OTHER' 

    
def road_surface(condition):
    keep = ['WET', 'DRY', 'OTHER', 'UNKNOWN']
    wet = ['SNOW OR SLUSH', 'ICE']
    if condition in keep:
        return condition
    elif condition in wet:
        return 'WET'
    else:
        return 'OTHER'

    
names = list(all_df.STREET_NAME.value_counts().sort_values()[1518:].index)
def street_acc(name):
    if name in names:
        return 'HIGH ACCIDENT RATE'
    else:
        return 'LOW ACCIDENT RATE'


def phys_cond(condition):
    keep = ['NORMAL', 'UNKNOWN', 'OTHER']
    substance = ['HAD BEEN DRINKING', 'MEDICATED']
    physical = ['FATIGUED/ASLEEP', 'EMOTIONAL', 'ILLNESS/FAINTED']
    if condition in keep:
        return condition
    elif 'IMPAIRED' in condition:
        return 'IMPAIRED'
    elif condition in substance:
        return 'IMPAIRED'
    elif condition in physical:
        return 'FATIGUE/ILL/EMOTION'
    else:
        return 'OTHER'

def primary(cause):
    keep = ['UNABLE TO DETERMINE', 'NOT APPLICABLE', 'WEATHER']
    construction = ['ROAD CONSTRUCTION/MAINTENANCE', 'ROAD ENGINEERING/SURFACE/MARKING DEFECTS']
    not_driver = ['VISION OBSCURED (SIGNS, TREE LIMBS, BUILDINGS, ETC.)', 
                  'EVASIVE ACTION DUE TO ANIMAL, OBJECT, NONMOTORIST', 'ANIMAL', 'OBSTRUCTED CROSSWALKS']
    if cause in keep:
        return cause
    elif cause in construction:
        return 'CONSTRUCTION'
    elif cause in not_driver:
        return 'NOT DRIVER FAULT'
    else:
        return 'DRIVER FAULT'