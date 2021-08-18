import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import plot_confusion_matrix, accuracy_score
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import warnings
warnings.filterwarnings('ignore')



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

    
def street_acc(name):
    #60 busiest streets in Chicago with accident rate of 3750 or more
    streets = ['HARRISON ST', 'VINCENNES AVE', 'CONGRESS PKWY', 'WASHINGTON BLVD', 'RACINE AVE', 'MARQUETTE RD', 'JACKSON BLVD',
             'LINCOLN AVE', 'BROADWAY', 'PETERSON AVE', 'ELSTON AVE', 'WENTWORTH AVE', 'KOSTNER AVE', 'MONTROSE AVE', '71ST ST',
             'LAKE ST', 'LARAMIE AVE', 'DIVERSEY AVE', 'OGDEN AVE', 'HARLEM AVE', 'LAWRENCE AVE', 'FOSTER AVE', 'LAKE SHORE DR',
             'DEVON AVE', 'CERMAK RD', 'SHERIDAN RD', '95TH ST', '47TH ST', 'MILWAUKEE AVE', 'DIVISION ST', 
             'DR MARTIN LUTHER KING JR DR', 'LAKE SHORE DR SB', 'ADDISON ST', 'LAKE SHORE DR NB', '79TH ST', 
             'COTTAGE GROVE AVE', 'MADISON ST', 'CHICAGO AVE', 'ROOSEVELT RD', '63RD ST', 'FULLERTON AVE', 'BELMONT AVE', 
             '87TH ST', 'ARCHER AVE', 'DAMEN AVE', 'CALIFORNIA AVE', 'IRVING PARK RD', 'CENTRAL AVE', 'GRAND AVE', 'CLARK ST',
             'STONY ISLAND AVE', 'NORTH AVE', 'STATE ST', 'MICHIGAN AVE', 'KEDZIE AVE', 'HALSTED ST', 'ASHLAND AVE', 
             'CICERO AVE', 'PULASKI RD', 'WESTERN AVE']

    if name in streets:
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
    
    
#FUNCTION FOR ITERATIVE MODEL RUNS
def run_model(X_train, X_test, y_train, y_test, model, target_names, scale=False):
    if scale:
        ss = StandardScaler()
        X_train_scaled = ss.fit_transform(X_train)
        X_test_scaled = ss.transform(X_test)
        model.fit(X_train_scaled, y_train)
        y_train_pred = model.predict(X_train_scaled)
        y_test_pred = model.predict(X_test_scaled)
        print(plot_confusion_matrix(model, X_train, y_train, cmap=plt.cm.Blues))
        print(classification_report(y_train, y_train_pred, target_names=target_names))
        print(plot_confusion_matrix(model, X_test, y_test, cmap=plt.cm.Blues))
        print(classification_report(y_test, y_test_pred, target_names=target_names))
        print("Training Accuracy Score: {}".format(model.score(X_train, y_train)))
        print("Testing Accuracy Score: {}".format(model.score(X_test, y_test)))
        return model

    model.fit(X_train, y_train)
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    print(plot_confusion_matrix(model, X_train, y_train, cmap=plt.cm.Blues))
    print(classification_report(y_train, y_train_pred, target_names=target_names))
    print(plot_confusion_matrix(model, X_test, y_test, cmap=plt.cm.Blues))
    print(classification_report(y_test, y_test_pred, target_names=target_names))
    print("Training Accuracy Score: {}".format(model.score(X_train, y_train)))
    print("Testing Accuracy Score: {}".format(model.score(X_test, y_test)))
    return model

#FUNCTION FOR OBTAIN AND GRAPSH FEATURE IMPORTANCES OF MODEL
def feature_importances(model, X_train):
    importance = model.feature_importances_
    columns = list(X_train.columns)
    df = pd.DataFrame(columns=['Feature', 'Importance'])
    df['Feature'] = columns
    df['Importance'] = importance
    df_sorted = df.sort_values(by='Importance', ascending = False)
    top_features = df_sorted['Feature'][0:12]
    top_importances = df_sorted['Importance'][0:12]
    
    plt.barh(top_features, top_importances)
    plt.title('Feature Importances')
    plt.show()