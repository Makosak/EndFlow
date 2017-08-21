import json
import cenpy as cp
import query_builder as qb


# This product uses the Census Bureau Data API but is not endorsed or certified
# by the Census Bureau.
# https://www.census.gov/data/developers/about/terms-of-service.html


API_SUMMARY = 'ACSSF5Y2015'    # This is the detail table (a.k.a. Summary File)
#API = 'ACSST5Y2015'    # This is the subject table
API_PROFILE = 'ACSProfile5Y2015'   # Profile 2015

KEY = json.load(open('/Users/erin/census_api_key.json'))['key']


# Found via https://census.missouri.edu/geocodes/?state=17#places
STATE = '17' # Illinois
COUNTY = '031' # Cook

# For joining
LEVEL = 'tract'
MERGE_FIELDS = ['GEOID','state','county',LEVEL]


def run_query(dicto,state,county,api,key):
    '''
    Runs the query for the specified dictionary, state, and county at the tract
    level using the supplied Census API and key.

    Inputs:  dicto:  A dictionary of dictionaries.
             state:  The two-digit FIPS ID for the desired state.
             county: The three-digit FIPS ID for the desired county.
    Outputs:  A pandas dataframe of the query results.

    Creates files:  None.
    '''

    cxn = cp.base.Connection(api, key)

    cols = qb.var_names(dicto)
    geo_unit = 'tract:*'#'block+group:*'
    geo_filter = {'state':state,'county':county}

    df = cxn.query(cols = cols, geo_unit = geo_unit, geo_filter = geo_filter)

    return df





if __name__ == '__main__':


    main_dicto = qb.build_main_dicto()
    ages_dicto = qb.build_ages_dicto()

    df_main = run_query(main_dicto,STATE,COUNTY,API_PROFILE,KEY)
    df_ages = run_query(ages_dicto,STATE,COUNTY,API_SUMMARY,KEY)

    df_merged = df_main.merge(df_ages, on = MERGE_FIELDS, how = 'outer')
    df_merged.to_csv('merged.csv', index = False)
