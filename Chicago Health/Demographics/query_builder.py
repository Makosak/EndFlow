import re


# This product uses the Census Bureau Data API but is not endorsed or certified
# by the Census Bureau.
# https://www.census.gov/data/developers/about/terms-of-service.html


def build_ages_dicto():
    '''
    Builds a dictionary of dictionaries.  The outer dictionary is keyed by topic
    area; the values are Census variable names, which are the keys in the inner
    dictionaries.  The values of the inner dictionaries are variable
    descriptions.

    API:  ACS 2015 5-YR Summary File (ACSSF5Y2015)

    Inputs:  None.
    Outputs:  A dictionary of dictionaries.

    Creates files:  None.
    '''

    dicto = {}

    # GeoID
    dicto['geoid'] = {'GEOID':'Geographic Identifier'}

    # Total population and age groups by sex
    dicto['sex_by_age'] = {'B01001_001E':'Total',
                           'B01001_001M':'Margin Of Error For!!Total',
                           'B01001_002E':'Male',
                           'B01001_002M':'Margin Of Error For!!Male',
                           'B01001_003E':'Male:!!Under 5 years',
                           'B01001_003M':'Margin Of Error For!!Male:!!Under 5 years',
                           'B01001_004E':'Male:!!5 to 9 years',
                           'B01001_004M':'Margin Of Error For!!Male:!!5 to 9 years',
                           'B01001_005E':'Male:!!10 to 14 years',
                           'B01001_005M':'Margin Of Error For!!Male:!!10 to 14 years',
                           'B01001_006E':'Male:!!15 to 17 years',
                           'B01001_006M':'Margin Of Error For!!Male:!!15 to 17 years',
                           'B01001_007E':'Male:!!18 and 19 years',
                           'B01001_007M':'Margin Of Error For!!Male:!!18 and 19 years',
                           'B01001_008E':'Male:!!20 years',
                           'B01001_008M':'Margin Of Error For!!Male:!!20 years',
                           'B01001_009E':'Male:!!21 years',
                           'B01001_009M':'Margin Of Error For!!Male:!!21 years',
                           'B01001_010E':'Male:!!22 to 24 years',
                           'B01001_010M':'Margin Of Error For!!Male:!!22 to 24 years',
                           'B01001_011E':'Male:!!25 to 29 years',
                           'B01001_011M':'Margin Of Error For!!Male:!!25 to 29 years',
                           'B01001_012E':'Male:!!30 to 34 years',
                           'B01001_012M':'Margin Of Error For!!Male:!!30 to 34 years',
                           'B01001_013E':'Male:!!35 to 39 years',
                           'B01001_013M':'Margin Of Error For!!Male:!!35 to 39 years',
                           'B01001_014E':'Male:!!40 to 44 years',
                           'B01001_014M':'Margin Of Error For!!Male:!!40 to 44 years',
                           'B01001_015E':'Male:!!45 to 49 years',
                           'B01001_015M':'Margin Of Error For!!Male:!!45 to 49 years',
                           'B01001_016E':'Male:!!50 to 54 years',
                           'B01001_016M':'Margin Of Error For!!Male:!!50 to 54 years',
                           'B01001_017E':'Male:!!55 to 59 years',
                           'B01001_017M':'Margin Of Error For!!Male:!!55 to 59 years',
                           'B01001_018E':'Male:!!60 and 61 years',
                           'B01001_018M':'Margin Of Error For!!Male:!!60 and 61 years',
                           'B01001_019E':'Male:!!62 to 64 years',
                           'B01001_019M':'Margin Of Error For!!Male:!!62 to 64 years',
                           'B01001_020E':'Male:!!65 and 66 years',
                           'B01001_020M':'Margin Of Error For!!Male:!!65 and 66 years',
                           'B01001_021E':'Male:!!67 to 69 years',
                           'B01001_021M':'Margin Of Error For!!Male:!!67 to 69 years',
                           'B01001_022E':'Male:!!70 to 74 years',
                           'B01001_022M':'Margin Of Error For!!Male:!!70 to 74 years',
                           'B01001_023E':'Male:!!75 to 79 years',
                           'B01001_023M':'Margin Of Error For!!Male:!!75 to 79 years',
                           'B01001_024E':'Male:!!80 to 84 years',
                           'B01001_024M':'Margin Of Error For!!Male:!!80 to 84 years',
                           'B01001_025E':'Male:!!85 years and over',
                           'B01001_025M':'Margin Of Error For!!Male:!!85 years and over',
                           'B01001_026E':'Female',
                           'B01001_026M':'Margin Of Error For!!Female',
                           'B01001_027E':'Female:!!Under 5 years',
                           'B01001_027M':'Margin Of Error For!!Female:!!Under 5 years',
                           'B01001_028E':'Female:!!5 to 9 years',
                           'B01001_028M':'Margin Of Error For!!Female:!!5 to 9 years',
                           'B01001_029E':'Female:!!10 to 14 years',
                           'B01001_029M':'Margin Of Error For!!Female:!!10 to 14 years',
                           'B01001_030E':'Female:!!15 to 17 years',
                           'B01001_030M':'Margin Of Error For!!Female:!!15 to 17 years',
                           'B01001_031E':'Female:!!18 and 19 years',
                           'B01001_031M':'Margin Of Error For!!Female:!!18 and 19 years',
                           'B01001_032E':'Female:!!20 years',
                           'B01001_032M':'Margin Of Error For!!Female:!!20 years',
                           'B01001_033E':'Female:!!21 years',
                           'B01001_033M':'Margin Of Error For!!Female:!!21 years',
                           'B01001_034E':'Female:!!22 to 24 years',
                           'B01001_034M':'Margin Of Error For!!Female:!!22 to 24 years',
                           'B01001_035E':'Female:!!25 to 29 years',
                           'B01001_035M':'Margin Of Error For!!Female:!!25 to 29 years',
                           'B01001_036E':'Female:!!30 to 34 years',
                           'B01001_036M':'Margin Of Error For!!Female:!!30 to 34 years',
                           'B01001_037E':'Female:!!35 to 39 years',
                           'B01001_037M':'Margin Of Error For!!Female:!!35 to 39 years',
                           'B01001_038E':'Female:!!40 to 44 years',
                           'B01001_038M':'Margin Of Error For!!Female:!!40 to 44 years',
                           'B01001_039E':'Female:!!45 to 49 years',
                           'B01001_039M':'Margin Of Error For!!Female:!!45 to 49 years',
                           'B01001_040E':'Female:!!50 to 54 years',
                           'B01001_040M':'Margin Of Error For!!Female:!!50 to 54 years',
                           'B01001_041E':'Female:!!55 to 59 years',
                           'B01001_041M':'Margin Of Error For!!Female:!!55 to 59 years',
                           'B01001_042E':'Female:!!60 and 61 years',
                           'B01001_042M':'Margin Of Error For!!Female:!!60 and 61 years',
                           'B01001_043E':'Female:!!62 to 64 years',
                           'B01001_043M':'Margin Of Error For!!Female:!!62 to 64 years',
                           'B01001_044E':'Female:!!65 and 66 years',
                           'B01001_044M':'Margin Of Error For!!Female:!!65 and 66 years',
                           'B01001_045E':'Female:!!67 to 69 years',
                           'B01001_045M':'Margin Of Error For!!Female:!!67 to 69 years',
                           'B01001_046E':'Female:!!70 to 74 years',
                           'B01001_046M':'Margin Of Error For!!Female:!!70 to 74 years',
                           'B01001_047E':'Female:!!75 to 79 years',
                           'B01001_047M':'Margin Of Error For!!Female:!!75 to 79 years',
                           'B01001_048E':'Female:!!80 to 84 years',
                           'B01001_048M':'Margin Of Error For!!Female:!!80 to 84 years',
                           'B01001_049E':'Female:!!85 years and over',
                           'B01001_049M':'Margin Of Error For!!Female:!!85 years and over'}

    # Run the dictionary through a function to fix the descriptions
    dicto = fix_vardescs(dicto)

    return dicto




def build_main_dicto():
    '''
    Builds a dictionary of dictionaries.  The outer dictionary is keyed by topic
    area; the values are Census variable names, which are the keys in the inner
    dictionaries.  The values of the inner dictionaries are variable
    descriptions.

    API:  ACS 2015 5-YR Profile (ACSProfile5Y2015)

    Inputs:  None.
    Outputs:  A dictionary of dictionaries.

    Creates files:  None.
    '''

    dicto = {}

    # GeoID
    dicto['geoid'] = {'GEOID':'Geographic Identifier'}

    # Race & ethnicity
    dicto['race_eth'] = {'DP05_0028E':'RACE!!Total population',
                         'DP05_0028M':'RACE!!Total population',
                         'DP05_0028PE':'RACE!!Total population',
                         'DP05_0028PM':'RACE!!Total population',
                         'DP05_0029E':'RACE!!Total population!!One race',
                         'DP05_0029M':'RACE!!Total population!!One race',
                         'DP05_0029PE':'RACE!!Total population!!One race',
                         'DP05_0029PM':'RACE!!Total population!!One race',
                         'DP05_0030E':'RACE!!Total population!!Two or more races',
                         'DP05_0030M':'RACE!!Total population!!Two or more races',
                         'DP05_0030PE':'RACE!!Total population!!Two or more races',
                         'DP05_0030PM':'RACE!!Total population!!Two or more races',
                         'DP05_0031E':'RACE!!One race',
                         'DP05_0031M':'RACE!!One race',
                         'DP05_0031PE':'RACE!!One race',
                         'DP05_0031PM':'RACE!!One race',
                         'DP05_0032E':'RACE!!One race!!White',
                         'DP05_0032M':'RACE!!One race!!White',
                         'DP05_0032PE':'RACE!!One race!!White',
                         'DP05_0032PM':'RACE!!One race!!White',
                         'DP05_0033E':'RACE!!One race!!Black or African American',
                         'DP05_0033M':'RACE!!One race!!Black or African American',
                         'DP05_0033PE':'RACE!!One race!!Black or African American',
                         'DP05_0033PM':'RACE!!One race!!Black or African American',
                         'DP05_0034E':'RACE!!One race!!American Indian and Alaska Native',
                         'DP05_0034M':'RACE!!One race!!American Indian and Alaska Native',
                         'DP05_0034PE':'RACE!!One race!!American Indian and Alaska Native',
                         'DP05_0034PM':'RACE!!One race!!American Indian and Alaska Native',
                         'DP05_0039E':'RACE!!One race!!Asian',
                         'DP05_0039M':'RACE!!One race!!Asian',
                         'DP05_0039PE':'RACE!!One race!!Asian',
                         'DP05_0039PM':'RACE!!One race!!Asian',
                         'DP05_0047E':'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0047M':'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0047PE':'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0047PM':'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0052E':'RACE!!One race!!Some other race',
                         'DP05_0052M':'RACE!!One race!!Some other race',
                         'DP05_0052PE':'RACE!!One race!!Some other race',
                         'DP05_0052PM':'RACE!!One race!!Some other race',
                         'DP05_0053E':'RACE!!Two or more races',
                         'DP05_0053M':'RACE!!Two or more races',
                         'DP05_0053PE':'RACE!!Two or more races',
                         'DP05_0053PM':'RACE!!Two or more races',
                         'DP05_0054E':'RACE!!Two or more races!!White and Black or African American',
                         'DP05_0054M':'RACE!!Two or more races!!White and Black or African American',
                         'DP05_0054PE':'RACE!!Two or more races!!White and Black or African American',
                         'DP05_0054PM':'RACE!!Two or more races!!White and Black or African American',
                         'DP05_0055E':'RACE!!Two or more races!!White and American Indian and Alaska Native',
                         'DP05_0055M':'RACE!!Two or more races!!White and American Indian and Alaska Native',
                         'DP05_0055PE':'RACE!!Two or more races!!White and American Indian and Alaska Native',
                         'DP05_0055PM':'RACE!!Two or more races!!White and American Indian and Alaska Native',
                         'DP05_0056E':'RACE!!Two or more races!!White and Asian',
                         'DP05_0056M':'RACE!!Two or more races!!White and Asian',
                         'DP05_0056PE':'RACE!!Two or more races!!White and Asian',
                         'DP05_0056PM':'RACE!!Two or more races!!White and Asian',
                         'DP05_0057E':'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                         'DP05_0057M':'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                         'DP05_0057PE':'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                         'DP05_0057PM':'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                         'DP05_0058E':'Race alone or in combination with one or more other races!!Total population',
                         'DP05_0058M':'Race alone or in combination with one or more other races!!Total population',
                         'DP05_0058PE':'Race alone or in combination with one or more other races!!Total population',
                         'DP05_0058PM':'Race alone or in combination with one or more other races!!Total population',
                         'DP05_0059E':'Race alone or in combination with one or more other races!!Total population!!White',
                         'DP05_0059M':'Race alone or in combination with one or more other races!!Total population!!White',
                         'DP05_0059PE':'Race alone or in combination with one or more other races!!Total population!!White',
                         'DP05_0059PM':'Race alone or in combination with one or more other races!!Total population!!White',
                         'DP05_0060E':'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                         'DP05_0060M':'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                         'DP05_0060PE':'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                         'DP05_0060PM':'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                         'DP05_0061E':'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                         'DP05_0061M':'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                         'DP05_0061PE':'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                         'DP05_0061PM':'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                         'DP05_0062E':'Race alone or in combination with one or more other races!!Total population!!Asian',
                         'DP05_0062M':'Race alone or in combination with one or more other races!!Total population!!Asian',
                         'DP05_0062PE':'Race alone or in combination with one or more other races!!Total population!!Asian',
                         'DP05_0062PM':'Race alone or in combination with one or more other races!!Total population!!Asian',
                         'DP05_0063E':'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0063M':'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0063PE':'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0063PM':'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                         'DP05_0064E':'Race alone or in combination with one or more other races!!Total population!!Some other race',
                         'DP05_0064M':'Race alone or in combination with one or more other races!!Total population!!Some other race',
                         'DP05_0064PE':'Race alone or in combination with one or more other races!!Total population!!Some other race',
                         'DP05_0064PM':'Race alone or in combination with one or more other races!!Total population!!Some other race',
                         'DP05_0065E':'HISPANIC OR LATINO AND RACE!!Total population',
                         'DP05_0065M':'HISPANIC OR LATINO AND RACE!!Total population',
                         'DP05_0065PE':'HISPANIC OR LATINO AND RACE!!Total population',
                         'DP05_0065PM':'HISPANIC OR LATINO AND RACE!!Total population',
                         'DP05_0066E':'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                         'DP05_0066M':'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                         'DP05_0066PE':'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                         'DP05_0066PM':'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                         'DP05_0071E':'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino',
                         'DP05_0071M':'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino',
                         'DP05_0071PE':'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino',
                         'DP05_0071PM':'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino'}

    # Household income brackets
    # Household Income in the Past 12 Months (in 2015 Inflation-Adjusted Dollars)
    dicto['hh_income'] = {'DP03_0051E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households',
                          'DP03_0051M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households',
                          'DP03_0051PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households',
                          'DP03_0051PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households',
                          'DP03_0052E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                          'DP03_0052M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                          'DP03_0052PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                          'DP03_0052PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Less than $10,000',
                          'DP03_0053E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                          'DP03_0053M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                          'DP03_0053PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                          'DP03_0053PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$10,000 to $14,999',
                          'DP03_0054E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                          'DP03_0054M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                          'DP03_0054PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                          'DP03_0054PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$15,000 to $24,999',
                          'DP03_0055E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                          'DP03_0055M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                          'DP03_0055PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                          'DP03_0055PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$25,000 to $34,999',
                          'DP03_0056E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                          'DP03_0056M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                          'DP03_0056PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                          'DP03_0056PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$35,000 to $49,999',
                          'DP03_0057E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                          'DP03_0057M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                          'DP03_0057PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                          'DP03_0057PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$50,000 to $74,999',
                          'DP03_0058E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                          'DP03_0058M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                          'DP03_0058PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                          'DP03_0058PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$75,000 to $99,999',
                          'DP03_0059E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                          'DP03_0059M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                          'DP03_0059PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                          'DP03_0059PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$100,000 to $149,999',
                          'DP03_0060E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                          'DP03_0060M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                          'DP03_0060PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                          'DP03_0060PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$150,000 to $199,999',
                          'DP03_0061E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more',
                          'DP03_0061M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more',
                          'DP03_0061PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more',
                          'DP03_0061PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!$200,000 or more'}

    # Other income variables
    dicto['other_income'] = {'DP03_0062E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Median household income (dollars)',
                             'DP03_0062M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Median household income (dollars)',
                             'DP03_0062PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Median household income (dollars)',
                             'DP03_0062PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Median household income (dollars)',
                             'DP03_0063E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Mean household income (dollars)',
                             'DP03_0063M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Mean household income (dollars)',
                             'DP03_0063PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Mean household income (dollars)',
                             'DP03_0063PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!Mean household income (dollars)'}

    # Education levels
    # Educational Attainment for the Population 25 Years and Over
    dicto['edu'] = {'DP02_0058E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over',
                    'DP02_0058M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over',
                    'DP02_0058PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over',
                    'DP02_0058PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over',
                    'DP02_0059E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                    'DP02_0059M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                    'DP02_0059PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                    'DP02_0059PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Less than 9th grade',
                    'DP02_0060E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                    'DP02_0060M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                    'DP02_0060PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                    'DP02_0060PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma',
                    'DP02_0061E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                    'DP02_0061M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                    'DP02_0061PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                    'DP02_0061PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)',
                    'DP02_0062E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                    'DP02_0062M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                    'DP02_0062PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                    'DP02_0062PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree',
                    'DP02_0063E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                    'DP02_0063M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                    'DP02_0063PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                    'DP02_0063PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate\'s degree',
                    'DP02_0064E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                    'DP02_0064M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                    'DP02_0064PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                    'DP02_0064PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor\'s degree',
                    'DP02_0065E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree',
                    'DP02_0065M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree',
                    'DP02_0065PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree',
                    'DP02_0065PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree',
                    'DP02_0066E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent high school graduate or higher',
                    'DP02_0066M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent high school graduate or higher',
                    'DP02_0066PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent high school graduate or higher',
                    'DP02_0066PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent high school graduate or higher',
                    'DP02_0067E':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent Bachelor\'s degree or higher',
                    'DP02_0067M':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent Bachelor\'s degree or higher',
                    'DP02_0067PE':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent Bachelor\'s degree or higher',
                    'DP02_0067PM':'EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Percent Bachelor\'s degree or higher'}

    # Household characteristics, including FHH
    dicto['households'] = {'DP02_0001E':'HOUSEHOLDS BY TYPE!!Total households',
                           'DP02_0001M':'HOUSEHOLDS BY TYPE!!Total households',
                           'DP02_0001PE':'HOUSEHOLDS BY TYPE!!Total households',
                           'DP02_0001PM':'HOUSEHOLDS BY TYPE!!Total households',
                           'DP02_0002E':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)',
                           'DP02_0002M':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)',
                           'DP02_0002PE':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)',
                           'DP02_0002PM':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)',
                           'DP02_0003E':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!With own children of the householder under 18 years',
                           'DP02_0003M':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!With own children of the householder under 18 years',
                           'DP02_0003PE':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!With own children of the householder under 18 years',
                           'DP02_0003PM':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!With own children of the householder under 18 years',
                           'DP02_0004E':'HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                           'DP02_0004M':'HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                           'DP02_0004PE':'HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                           'DP02_0004PM':'HOUSEHOLDS BY TYPE!!Total households!!Married-couple family',
                           'DP02_0005E':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Married-couple family!!With own children of the householder under 18 years',
                           'DP02_0005M':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Married-couple family!!With own children of the householder under 18 years',
                           'DP02_0005PE':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Married-couple family!!With own children of the householder under 18 years',
                           'DP02_0005PM':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Married-couple family!!With own children of the householder under 18 years',
                           'DP02_0006E':'HOUSEHOLDS BY TYPE!!Total households!!Male householder, no wife present, family',
                           'DP02_0006M':'HOUSEHOLDS BY TYPE!!Total households!!Male householder, no wife present, family',
                           'DP02_0006PE':'HOUSEHOLDS BY TYPE!!Total households!!Male householder, no wife present, family',
                           'DP02_0006PM':'HOUSEHOLDS BY TYPE!!Total households!!Male householder, no wife present, family',
                           'DP02_0007E':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Male householder, no wife present, family!!With own children of the householder under 18 years',
                           'DP02_0007M':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Male householder, no wife present, family!!With own children of the householder under 18 years',
                           'DP02_0007PE':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Male householder, no wife present, family!!With own children of the householder under 18 years',
                           'DP02_0007PM':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Male householder, no wife present, family!!With own children of the householder under 18 years',
                           'DP02_0008E':'HOUSEHOLDS BY TYPE!!Total households!!Female householder, no husband present, family',
                           'DP02_0008M':'HOUSEHOLDS BY TYPE!!Total households!!Female householder, no husband present, family',
                           'DP02_0008PE':'HOUSEHOLDS BY TYPE!!Total households!!Female householder, no husband present, family',
                           'DP02_0008PM':'HOUSEHOLDS BY TYPE!!Total households!!Female householder, no husband present, family',
                           'DP02_0009E':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Female householder, no husband present, family!!With own children of the householder under 18 years',
                           'DP02_0009M':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Female householder, no husband present, family!!With own children of the householder under 18 years',
                           'DP02_0009PE':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Female householder, no husband present, family!!With own children of the householder under 18 years',
                           'DP02_0009PM':'HOUSEHOLDS BY TYPE!!Total households!!Family households (families)!!Female householder, no husband present, family!!With own children of the householder under 18 years',
                           'DP02_0010E':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households',
                           'DP02_0010M':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households',
                           'DP02_0010PE':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households',
                           'DP02_0010PM':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households',
                           'DP02_0011E':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone',
                           'DP02_0011M':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone',
                           'DP02_0011PE':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone',
                           'DP02_0011PM':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone',
                           'DP02_0012E':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over',
                           'DP02_0012M':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over',
                           'DP02_0012PE':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over',
                           'DP02_0012PM':'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over',
                           'DP02_0013E':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people under 18 years',
                           'DP02_0013M':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people under 18 years',
                           'DP02_0013PE':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people under 18 years',
                           'DP02_0013PM':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people under 18 years',
                           'DP02_0014E':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over',
                           'DP02_0014M':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over',
                           'DP02_0014PE':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over',
                           'DP02_0014PM':'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over',
                           'DP02_0015E':'HOUSEHOLDS BY TYPE!!Total households!!Average household size',
                           'DP02_0015M':'HOUSEHOLDS BY TYPE!!Total households!!Average household size',
                           'DP02_0015PE':'HOUSEHOLDS BY TYPE!!Total households!!Average household size',
                           'DP02_0015PM':'HOUSEHOLDS BY TYPE!!Total households!!Average household size',
                           'DP02_0016E':'HOUSEHOLDS BY TYPE!!Total households!!Average family size',
                           'DP02_0016M':'HOUSEHOLDS BY TYPE!!Total households!!Average family size',
                           'DP02_0016PE':'HOUSEHOLDS BY TYPE!!Total households!!Average family size',
                           'DP02_0016PM':'HOUSEHOLDS BY TYPE!!Total households!!Average family size'}

    # Employment
    dicto['employment'] = {'DP03_0001E':'EMPLOYMENT STATUS!!Population 16 years and over',
                           'DP03_0001M':'EMPLOYMENT STATUS!!Population 16 years and over',
                           'DP03_0001PE':'EMPLOYMENT STATUS!!Population 16 years and over',
                           'DP03_0001PM':'EMPLOYMENT STATUS!!Population 16 years and over',
                           'DP03_0002E':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force',
                           'DP03_0002M':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force',
                           'DP03_0002PE':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force',
                           'DP03_0002PM':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force',
                           'DP03_0003E':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0003M':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0003PE':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0003PM':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0004E':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                           'DP03_0004M':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                           'DP03_0004PE':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                           'DP03_0004PM':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Employed',
                           'DP03_0005E':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                           'DP03_0005M':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                           'DP03_0005PE':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                           'DP03_0005PM':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed',
                           'DP03_0006E':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                           'DP03_0006M':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                           'DP03_0006PE':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                           'DP03_0006PM':'EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Armed Forces',
                           'DP03_0007E':'EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force',
                           'DP03_0007M':'EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force',
                           'DP03_0007PE':'EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force',
                           'DP03_0007PM':'EMPLOYMENT STATUS!!Population 16 years and over!!Not in labor force',
                           'DP03_0008E':'EMPLOYMENT STATUS!!Civilian labor force',
                           'DP03_0008M':'EMPLOYMENT STATUS!!Civilian labor force',
                           'DP03_0008PE':'EMPLOYMENT STATUS!!Civilian labor force',
                           'DP03_0008PM':'EMPLOYMENT STATUS!!Civilian labor force',
                           'DP03_0009E':'EMPLOYMENT STATUS!!Civilian labor force!!Unemployment Rate',
                           'DP03_0009M':'EMPLOYMENT STATUS!!Civilian labor force!!Unemployment Rate',
                           'DP03_0009PE':'EMPLOYMENT STATUS!!Civilian labor force!!Unemployment Rate',
                           'DP03_0009PM':'EMPLOYMENT STATUS!!Civilian labor force!!Unemployment Rate',
                           'DP03_0010E':'EMPLOYMENT STATUS!!Females 16 years and over',
                           'DP03_0010M':'EMPLOYMENT STATUS!!Females 16 years and over',
                           'DP03_0010PE':'EMPLOYMENT STATUS!!Females 16 years and over',
                           'DP03_0010PM':'EMPLOYMENT STATUS!!Females 16 years and over',
                           'DP03_0011E':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force',
                           'DP03_0011M':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force',
                           'DP03_0011PE':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force',
                           'DP03_0011PM':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force',
                           'DP03_0012E':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0012M':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0012PE':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0012PM':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force',
                           'DP03_0013E':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force!!Employed',
                           'DP03_0013M':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force!!Employed',
                           'DP03_0013PE':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force!!Employed',
                           'DP03_0013PM':'EMPLOYMENT STATUS!!Females 16 years and over!!In labor force!!Civilian labor force!!Employed'}

    # Housing burden
    # Gross Rent/Mortgage as a Percentage of Household Income
    dicto['housing_burden'] = {'DP04_0110E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0110M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0110PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0110PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0111E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 20.0 percent',
                               'DP04_0111M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 20.0 percent',
                               'DP04_0111PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 20.0 percent',
                               'DP04_0111PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 20.0 percent',
                               'DP04_0112E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0112M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0112PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0112PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0113E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0113M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0113PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0113PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0114E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0114M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0114PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0114PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0115E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0115M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0115PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0115PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0116E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0116M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0116PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0116PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing units with a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0117E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0117M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0117PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0117PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)',
                               'DP04_0118E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 10.0 percent',
                               'DP04_0118M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 10.0 percent',
                               'DP04_0118PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 10.0 percent',
                               'DP04_0118PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Less than 10.0 percent',
                               'DP04_0119E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!10.0 to 14.9 percent',
                               'DP04_0119M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!10.0 to 14.9 percent',
                               'DP04_0119PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!10.0 to 14.9 percent',
                               'DP04_0119PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!10.0 to 14.9 percent',
                               'DP04_0120E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0120M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0120PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0120PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0121E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0121M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0121PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0121PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0122E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0122M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0122PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0122PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0123E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0123M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0123PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0123PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0124E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0124M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0124PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0124PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0125E':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0125M':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0125PE':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0125PM':'SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME (SMOCAPI)!!Housing unit without a mortgage (excluding units where SMOCAPI cannot be computed)!!Not computed',
                               'DP04_0136E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)',
                               'DP04_0136M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)',
                               'DP04_0136PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)',
                               'DP04_0136PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)',
                               'DP04_0137E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Less than 15.0 percent',
                               'DP04_0137M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Less than 15.0 percent',
                               'DP04_0137PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Less than 15.0 percent',
                               'DP04_0137PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Less than 15.0 percent',
                               'DP04_0138E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0138M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0138PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0138PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!15.0 to 19.9 percent',
                               'DP04_0139E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0139M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0139PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0139PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!20.0 to 24.9 percent',
                               'DP04_0140E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0140M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0140PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0140PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!25.0 to 29.9 percent',
                               'DP04_0141E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0141M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0141PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0141PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!30.0 to 34.9 percent',
                               'DP04_0142E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0142M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0142PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0142PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!35.0 percent or more',
                               'DP04_0143E':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Not computed',
                               'DP04_0143M':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Not computed',
                               'DP04_0143PE':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Not computed',
                               'DP04_0143PM':'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME (GRAPI)!!Occupied units paying rent (excluding units where GRAPI cannot be computed)!!Not computed'}

    # Housing tenure
    dicto['housing_tenure'] = {'DP04_0045E':'HOUSING TENURE!!Occupied housing units',
                               'DP04_0045M':'HOUSING TENURE!!Occupied housing units',
                               'DP04_0045PE':'HOUSING TENURE!!Occupied housing units',
                               'DP04_0045PM':'HOUSING TENURE!!Occupied housing units',
                               'DP04_0046E':'HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                               'DP04_0046M':'HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                               'DP04_0046PE':'HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                               'DP04_0046PM':'HOUSING TENURE!!Occupied housing units!!Owner-occupied',
                               'DP04_0047E':'HOUSING TENURE!!Occupied housing units!!Renter-occupied',
                               'DP04_0047M':'HOUSING TENURE!!Occupied housing units!!Renter-occupied',
                               'DP04_0047PE':'HOUSING TENURE!!Occupied housing units!!Renter-occupied',
                               'DP04_0047PM':'HOUSING TENURE!!Occupied housing units!!Renter-occupied'}

    # Nativity
    dicto['nativity'] = {'DP02_0086E':'PLACE OF BIRTH!!Total population',
                         'DP02_0086M':'PLACE OF BIRTH!!Total population',
                         'DP02_0086PE':'PLACE OF BIRTH!!Total population',
                         'DP02_0086PM':'PLACE OF BIRTH!!Total population',
                         'DP02_0087E':'PLACE OF BIRTH!!Total population!!Native',
                         'DP02_0087M':'PLACE OF BIRTH!!Total population!!Native',
                         'DP02_0087PE':'PLACE OF BIRTH!!Total population!!Native',
                         'DP02_0087PM':'PLACE OF BIRTH!!Total population!!Native',
                         'DP02_0092E':'PLACE OF BIRTH!!Total population!!Foreign born',
                         'DP02_0092M':'PLACE OF BIRTH!!Total population!!Foreign born',
                         'DP02_0092PE':'PLACE OF BIRTH!!Total population!!Foreign born',
                         'DP02_0092PM':'PLACE OF BIRTH!!Total population!!Foreign born'}

    # Public assistance
    dicto['public_assistance'] = {'DP03_0070E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income',
                                  'DP03_0070M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income',
                                  'DP03_0070PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income',
                                  'DP03_0070PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income',
                                  'DP03_0071E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income!!Mean Supplemental Security Income (dollars)',
                                  'DP03_0071M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income!!Mean Supplemental Security Income (dollars)',
                                  'DP03_0071PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income!!Mean Supplemental Security Income (dollars)',
                                  'DP03_0071PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Supplemental Security Income!!Mean Supplemental Security Income (dollars)',
                                  'DP03_0072E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income',
                                  'DP03_0072M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income',
                                  'DP03_0072PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income',
                                  'DP03_0072PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income',
                                  'DP03_0073E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income!!Mean cash public assistance income (dollars)',
                                  'DP03_0073M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income!!Mean cash public assistance income (dollars)',
                                  'DP03_0073PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income!!Mean cash public assistance income (dollars)',
                                  'DP03_0073PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With cash public assistance income!!Mean cash public assistance income (dollars)',
                                  'DP03_0074E':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months',
                                  'DP03_0074M':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months',
                                  'DP03_0074PE':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months',
                                  'DP03_0074PM':'INCOME AND BENEFITS (IN 2015 INFLATION-ADJUSTED DOLLARS)!!Total households!!With Food Stamp/SNAP benefits in the past 12 months'}

    # Run the dictionary through a function to fix the descriptions
    dicto = fix_vardescs(dicto)

    return dicto


def fix_vardescs(dicto):
    '''
    Fixes the variable descriptions in the dictionary in the following ways:
    - Replaces instances of '!!' with ' - '
    - Labels each variable as an Estimate, Estimate Margin of Error (MOE),
     Percent, or Percent MOE, as appropriate
    '''

    for okey in dicto.keys():
        for item in dicto[okey].items():
            ikey, ivalue = item
            ivalue = ivalue.replace('!!',' - ')
            if re.findall(r'_0*[0-9]+E', ikey):
                suffix = ' - Estimate'
            elif re.findall(r'_0*[0-9]+M', ikey):
                suffix = ' - Estimate MOE'
            elif re.findall(r'_0*[0-9]+PE', ikey):
                suffix = ' - Percent'
            elif re.findall(r'_0*[0-9]+PM', ikey):
                suffix = ' - Percent MOE'
            else:
                suffix = ''
            dicto[okey][ikey] = ivalue + suffix

    return dicto


def var_names(dicto):
    '''
    Given a dictionary, returns a list of Census variable names.

    Inputs:  dicto (dictionary): A dictionary of dictionaries.
    Outputs:  A list of Census variable names.

    Creates files:  None.
    '''

    var_list = []

    for iDicto in dicto.values():
        for iKey in iDicto.keys():
            var_list.append(iKey)

    return var_list
