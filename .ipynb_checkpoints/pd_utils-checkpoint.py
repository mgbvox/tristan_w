import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm
import pycountry
import pycountry_convert as pc

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b
    
def to_float(x): 
    if x:
        try: 
            res = float(x)
            return res
        except:
            return np.nan
    return np.nan

def search(term, df):
    res = []
    for c in tqdm(df.columns):
        if (term in df[c].values) or (str(term) in df[c].values):
            res.append(c)
    return res

def get_continent(country):
    country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
    continent_name = pc.country_alpha2_to_continent_code(country_code)
    return continent_name

def parse_continents(s):
    try:
        code = get_continent(s)
        return code
    except:
        return np.nan