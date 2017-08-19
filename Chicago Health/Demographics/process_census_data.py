import numpy as np
import pandas as pd
from string import digits
import query_builder as qb
from bidict import bidict as bd

# This product uses the Census Bureau Data API but is not endorsed or certified
# by the Census Bureau.
# https://www.census.gov/data/developers/about/terms-of-service.html


FI = 'merged.csv'

# For indexing in transformations
G = 'GEOID'
T = 'tract'
TOTAL = 'B01001_001E' # The variable containing the estimate of the total pop

AGE_CATS = [10,25,35,45,55,65] # Want 0-9, 10-24, etc.

R_1RACE = 'One race'
R_WHITE = 'White'
R_BLACK = 'Black or African American'
R_NATIV = 'American Indian and Alaska Native'
R_ASIAN = 'Asian'
R_NHWPI = 'Native Hawaiian and Other Pacific Islander'
R_OTHER = 'Some other race'
R_2PLUS = 'Two or more races'
E_HSPNC = 'Hispanic or Latino (of any race)'
E_NOTHS = 'Not Hispanic or Latino'


def calc_pct_gender(df):
    '''
    '''
    t = 'B01001_001E'
    m = 'B01001_002E'
    f = 'B01001_026E'

    pctM = 'PopulationPctMale'
    pctF = 'PopulationPctFemale'

    sub = pd.concat([df[T],df[B],df[t],df[m],df[f]], axis = 1)
    sub[pctM] = sub[m] / sub[t] * 100
    sub[pctF] = sub[f] / sub[t] * 100

    local_df = pd.concat([sub[T],sub[B],sub[pctM],sub[pctF]], axis = 1)

    return local_df


def find_lower_upper(keys,age_cats):
    '''
    '''

    low = 99
    high = 0

    for key in keys:
        val = age_cats[key]
        if len(val) == 1:
            if val < low:
                low = val
                l_key = key
            if val > high:
                high = val
                u_key = key

    return low, high, l_key, u_key


def split_age_vars(keys,age_cats_gender,age_cats):
    '''
    '''

    low, high, l_key, u_key = find_lower_upper(keys,age_cats_gender)

    values = list(age_cats_gender.values())
    values.sort()

    for age in age_cats:
        if age < low:
            continue
        elif age == low:
            continue


def split_census_variables(gender_dicto,age_cats,up_down):
    '''
    Takes in the gender_dicto, age_cats list, and up_down string and determines
    the Census variables that should be summed to create each gender-divided age
    range.

    Returns a dictionary of dictionaries.  The top-level keys are 'male' and
    'female'; the lower-level keys are the age brackets, and the value for each
    lower-level key is a list of the variables that should be summed to create
    the appropriate age range for that gender.
    '''

    assert up_down.lower() == 'up' or up_down.lower() == 'down', 'The up/down '\
        + 'string must equal \'up\' or \'down\'.\n'

    lowest = 0
    highest = 120

    dicto = {'female':{},'male':{}}

    for gender in dicto.keys():
        current_min = 0
        local_dicto = bd(gender_dicto[gender])
        vals_list = list(local_dicto.items())
        local_brackets = []
        for varname, bracket in vals_list:
            if len(bracket) == 2:
                local_brackets.append(bracket)
            else:
                local_brackets.append(tuple((bracket[0],bracket[0])))

        added = []

        for desired_break in age_cats + [120]:
            varname_list = []
            for bracket in local_brackets:
                l, h = bracket
                if up_down.lower() == 'up':
                    if desired_break <= l and desired_break < h or desired_break == h:
                        varname_list.append(local_dicto.inv[bracket])
                        current_max = h
                        if added:
                            last_added = added[-1]
                            last_idx = varname_list.index(last_added)
                            start_idx = last_idx + 1
                        else:
                            start_idx = 0
                        dicto[gender][tuple((current_min,current_max))] = varname_list[start_idx:]
                        current_min = h + 1
                        for item in varname_list[start_idx:]:
                            added.append(item)
                        varname_list = []
                        break
                    else:
                        varname_list.append(local_dicto.inv[bracket])
                else: # up_down.lower() == 'down'
                    if desired_break > l and desired_break - 1 == h or desired_break == l or desired_break == h:
                        varname_list.append(local_dicto.inv[bracket])
                        current_max = h
                        if added:
                            last_added = added[-1]
                            last_idx = varname_list.index(last_added)
                            start_idx = last_idx + 1
                        else:
                            start_idx = 0
                        dicto[gender][tuple((current_min,current_max))] = varname_list[start_idx:]
                        current_min = h + 1
                        for item in varname_list[start_idx:]:
                            added.append(item)
                        varname_list = []
                        break
                    else:
                        varname_list.append(local_dicto.inv[bracket])


    return dicto








'''
#def make_age_ranges(age_values,age_cats,up_down):
def make_age_ranges(gender_dicto,age_cats,up_down):
    ''
    Takes in a sorted list of integers that define the minimum values for the
    desired age categories and a string that specifies whether category breaks
    should be rounded up or down to the nearest Census break.

    Inputs:
    age_values:  A list of tuples that specify the age ranges used in the Census
                 variables.
    age_cats:    A sorted list of integers that define the minimum values for
                 the desired age categories.
    up_down:     A string, either  'up' or 'down' (case insensitive), specifying
                 the rounding method.

    Outputs:

    Creates files:  None.
    ''

    assert up_down.lower() == 'up' or up_down.lower() == 'down', 'The up/down '\
        + 'string must equal \'up\' or \'down\'.\n'

    low = 0
    high = 120

    # 'male' chosen arbitrarily; the breaks are the same for each gender
    age_values = list(gender_dicto['male'].values())

    # Start by initializing a list: tuple((0,4))
    local_vals = [tuple((low,age_values[0][0] - 1))]

    for bracket in age_values[1:-1]:
        # If it's a real bracket, append the bracket
        if len(bracket) == 2:
            local_vals.append(bracket)
        # Else, append a pseudobracket with the same start and end
        else:
            local_vals.append(tuple((bracket[0],bracket[0])))

    # Append the tuple((85,120)) bracket
    local_vals.append(tuple((age_values[-1][0],high)))

    # Create a set to which the break values will be added
    breaks = set([low])

    # Create a list of indices that tell which variables in the gender_dicto
    # are the starting point for an age range.
    census_idx = [low]

    for desired_break in age_cats:
        j = census_idx[-1]
        for i, census_breaks in enumerate(local_vals[j:]):
            lower, higher = census_breaks
            if up_down.lower() == 'up':
                if desired_break <= lower:
                    break_val = lower
                    idx = i + j
                    break
            else: # up_down.lower() == 'down'
                if desired_break < lower:
                    if desired_break >= higher:
                        break_val = lower
                        idx = i + j
                        break
                elif desired_break == lower:
                    break_val = lower
                    idx = i + j
                    break
        j += 1
        breaks.add(break_val)
        census_idx.append(idx)

    ranges = []

    breaks_list = list(breaks)
    breaks_list.sort()

    for i, age in enumerate(breaks_list[:-1]):
        ranges.append(str(age) + '-' + str(breaks_list[i+1] - 1))

    ranges.append(str(breaks_list[-1]) + ' and over')

    return census_idx, ranges
'''



def sum_age_ranges(df,age_cats_male,age_cats_female,age_cats):
    '''
    '''

    keysM = age_cats_male.keys()
    keysF = age_cats_female.keys()

    var_list = [T,B] + list(keysM) + list(keysF)

    local_df = pd.concat([df[x] for x in var_list], axis = 1)

    '''
    dicto['male'] = [['0-9',[var1,var2,var3]],
                     ['10-24',[var1,var2,var3,var4,var5]],
                     ['25-34',[var1]],
                      etc.]))
    '''

    return local_df









def make_gender_dicto(ages_dicto):
    '''
    '''

    dicto = {}

    dicto['male'] = dicto_age_cats_by_gender(ages_dicto,'male')
    dicto['female'] = dicto_age_cats_by_gender(ages_dicto,'female')

    return dicto


def dicto_age_cats_by_gender(dicto,gender):
    '''
    '''

    m, f = 'male', 'female'

    assert gender.lower() == m or gender.lower() == f, 'Gender must' \
        + ' equal \'Male\' or \'Female\'.\n'

    local_dicto = bd({})

    max_val = 0

    for key, value in dicto['sex_by_age'].items():
        if gender.title() in value and value.endswith('Estimate') and 'years' in value:
            limits = []
            split_val = value.split()
            for val in split_val:
                if val[0] in digits:
                    limits.append(int(val))
                    if int(val) > max_val:
                        max_val = int(val)

            if len(local_dicto) == 0:
                local_dicto[key] = tuple([0] + [limits[0] - 1])
            elif len(limits) == 1:
                local_dicto[key] = tuple(limits + limits)
            else:
                local_dicto[key] = tuple(limits)

    max_key = local_dicto.inv[tuple((max_val,max_val))]
    local_dicto[max_key] = tuple((max_val,120))

    return local_dicto


def process_ages(df,main_dicto,split):
    '''
    '''

    # For each gender in split
        # For each bracket in gender
            # Subset df to keep only those columns, then sum them and name them
            # with the gender and bracket

    # MAKE A LOCAL DF; initialize with the GEOID and the total pop
    new_df = df[[G,TOTAL]]

    for gender in split.keys():
        for bracket in split[gender].keys():
            low, high = bracket
            if high == 120:
                label = gender.upper() + ': ' + str(low) + ' and over - Estimate'
                pct_label = gender.upper() + ': ' + str(low) + ' and over - Percent'
            else:
                label = gender.upper() + ': ' + str(low) + '-' + str(high) + ' - Estimate'
                pct_label = gender.upper() + ': ' + str(low) + '-' + str(high) + ' - Percent'
            keep = split[gender][bracket]
            new_df[label]= df[keep].sum(axis=1)
            new_df[pct_label] = new_df[label] / new_df[TOTAL] * 100

    new_df = new_df.rename(index=str, columns={TOTAL:'Total population - Estimate'})

    new_df = new_df.set_index([G])

    return new_df



if __name__ == '__main__':

    main_dicto = qb.build_main_dicto()
    ages_dicto = qb.build_ages_dicto()

    df = pd.read_csv(FI)

    gender_dicto = make_gender_dicto(ages_dicto)

    split = split_census_variables(gender_dicto,AGE_CATS,'down')

    ages_df = process_ages(df,main_dicto,split)

    #census_idx, age_ranges = make_age_ranges(gender_dicto,AGE_CATS,'up')

    '''
    #df_dicto = {}
    #df_dicto['pct_gender'] = calc_pct_gender(df)
    #df_dicto['pctAgeCats'] = calc_ages(df,AGE_CATS.sort())
    age_cats_male = dicto_age_cats_by_gender(dicto,'male')
    age_cats_female = dicto_age_cats_by_gender(dicto,'female')
    vals = list(age_cats_male.values())
    census_idx, age_ranges = make_age_ranges(vals,AGE_CATS,'up')
    '''
