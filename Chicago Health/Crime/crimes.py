import numpy as np
import pandas as pd

FNAME = 'Crimes_-_2001_to_present.csv'
URL = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'

START = 2013
END = 2016



def read_file(mode):
    '''
    Reads in the Chicago Crimes 2001-present CSV, either from a local file or by
    downloading it from the Chicago Data Portal. The user sets the mode; when it
    equals 1, then the file is read locally; otherwise, the file is downloaded.

    Keeps only the necessary columns and events occurring in the specified year
    range. Additionally, keeps only events with certain IUCR codes. Drops
    observations that do not contain a latitude or longitude (or that contain a
    coordinate outside of Chicago). Creates a 'Category' column that classifies
    each offense according to its IUCR code.

    Returns a pandas dataframe.
    '''

    if mode == 1:
        source = FNAME
    else:
        source = URL

    nm = ['ID','Case Number','Date','Block','IUCR','Primary Type','Description',
          'Location Description','Arrest','Domestic','Beat','District','Ward',
          'Community Area','FBI Code','X Coordinate','Y Coordinate','Year',
          'Updated On','Latitude','Longitude','Location']

    uc = ['IUCR','Domestic','Community Area','Year','Latitude','Longitude']

    df = pd.read_csv(source, names = nm, usecols = uc,  skiprows = 1)

    df = df[df.Year >= START]
    df = df[df.Year <= END]

    dicto = iucr_recoder()

    df = df[df.IUCR.isin(dicto.keys())]

    df = df[np.isfinite(df.Latitude)]
    df = df[df.Latitude >= 41.64]
    df = df[df.Latitude <= 42.1]
    df = df[np.isfinite(df.Longitude)]
    df = df[df.Longitude >= -87.93]
    df = df[df.Longitude <= -87.52]

    df['Category'] = df.IUCR.apply(lambda x: dicto[x])

    return df.reset_index(drop = True)


def iucr_recoder():
    '''
    Creates a dictionary mapping IUCR codes to their respective categories.
    '''

    dicto_codes = {1:'Homicide',2:'Sexual Assault',3:'Non-Fatal Shooting',
                   4:'Robbery',5:'Battery',6:'Aggravated Assault',
                   7:'Substance-Related'}

    homicide = ['0110','0130']

    sexual_assault = ['0262','0263','0264','0265','0266','0271','0272','0273',
                      '0274','0275','0281','0291','0261']

    nonfatal_shooting = ['041A','041B','0450','0451','0480','0481','0488',
                         '0489']

    robbery = ['0312','0313','031A','031B','0320','0325','0326','0330','0331',
               '0334','0337','033A','033B','0340']

    battery = ['0420','0430','0440','0452','0453','0454','0460','0461','0462',
               '0475','0479','0482','0483','0484','0485','0486','0487','0495',
               '0496','0497','0498']

    aggravated_assault = ['051B','0520','0530','0545','0550','0551','0552',
                          '0553','0554','0555','0556','0557','0558','051B']

    substance = ['1811','1812','1821','1822','1840','1850','1860','1900','2010',
                 '2011','2012','2013','2014','2015','2016','2017','2018','2019',
                 '2020','2021','2022','2023','2024','2025','2026','2027','2028',
                 '2029','2030','2031','2032','2033','2034','2040','2050','2060',
                 '2070','2080','2090','2091','2092','2093','2094','2095','2110',
                 '2111','2120','2160','2170','1479'] # Need to add DWI codes

    dicto = {}

    for x in homicide:
        dicto[x] = dicto_codes[1]

    for x in sexual_assault:
        dicto[x] = dicto_codes[2]

    for x in nonfatal_shooting:
        dicto[x] = dicto_codes[3]

    for x in robbery:
        dicto[x] = dicto_codes[4]

    for x in battery:
        dicto[x] = dicto_codes[5]

    for x in aggravated_assault:
        dicto[x] = dicto_codes[6]

    for x in substance:
        dicto[x] = dicto_codes[7]

    return dicto



if __name__ == '__main__':
    # To read from a local CSV:  set mode to 1
    # To download file from portal, set mode to an integer not equal to 1
    mode = 1

    df = read_file(mode)

    # Process file and write to CSV
    df.to_csv('crimes.csv', index = False)
