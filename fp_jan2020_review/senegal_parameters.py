'''
Set the parameters for LEMOD-FP.
'''

import os
import pylab as pl
import pandas as pd
import sciris as sc

#%% Parameters for the calibration etc.

def abspath(path):
    cwd = os.path.abspath(os.path.dirname(__file__))
    output = os.path.join(cwd, path)
    return output

# pop_pyr_1982_fn = abspath('data/senegal-population-pyramid-1982.csv')
popsize_tfr_fn = abspath('data/senegal-popsize-tfr.csv')

# Load data
# pop_pyr_1982 = pd.read_csv(pop_pyr_1982_fn)
popsize_tfr  = pd.read_csv(popsize_tfr_fn, header=None)

# Handle population size
scale_factor = 2
years = popsize_tfr.iloc[0,:].to_numpy()
popsize = popsize_tfr.iloc[1,:].to_numpy() / 1000 * scale_factor




#%% Set parameters for the simulation

def default_age_pyramid():
    ''' Starting age bin, male population, female population ''' 
    # Based on Senegal 1982
    # pyramid = pl.array([[0,  579035, 567499],
    #                     [5,  459255, 452873],
    #                     [10, 364432, 359925],
    #                     [15, 294589, 292235],
    #                     [20, 239825, 241363],
    #                     [25, 195652, 198326],
    #                     [30, 155765, 158950],
    #                     [35, 135953, 137097],
    #                     [40, 124615, 122950],
    #                     [45, 107622, 106116],
    #                     [50,  89533, 89654],
    #                     [55,  70781, 73290],
    #                     [60,  52495, 57330],
    #                     [65,  36048, 41585],
    #                     [70,  21727, 26383],
    #                     [75,  10626, 13542],
    #                     [80,   4766,  6424]])
    
    pyramid = pl.array([ [0,  318225,  314011], # Senegal 1962
                         [5,  249054,  244271],
                        [10,  191209,  190998],
                        [15,  157800,  159536],
                        [20,  141480,  141717],
                        [25,  125002,  124293],
                        [30,  109339,  107802],
                        [35,  93359,   92119],
                        [40,  77605,   78231],
                        [45,  63650,   66117],
                        [50,  51038,   54934],
                        [55,  39715,   44202],
                        [60,  29401,   33497],
                        [65,  19522,   23019],
                        [70,  11686,   14167],
                        [75,  5985,    7390],
                        [80,  2875,    3554],
                    ])
    
    return pyramid
    

def default_age_mortality():
    ''' Age-dependent mortality rates -- see age_dependent_mortality.py in the fp_analyses repository '''
    mortality = {
            'bins': pl.array([ 0,  5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]), 
            'm': pl.array([0.01365168, 0.00580404, 0.00180847, 0.0012517 , 0.00171919, 0.00226466, 0.00258822, 0.00304351, 0.00377434, 0.00496091, 0.00694581, 0.01035062, 0.01563918, 0.02397286, 0.03651509,0.05578357, 0.08468156, 0.12539009, 0.17939655, 0.24558742]), 
            'f': pl.array([0.01213076, 0.00624896, 0.0017323 , 0.00114656, 0.00143726, 0.00175446, 0.00191577, 0.00214836, 0.00251644, 0.00315836, 0.00439748, 0.00638658, 0.00965512, 0.01506286, 0.02361487, 0.03781285, 0.06007898, 0.09345669, 0.14091699, 0.20357825]), }
    
    # TODO! WARNING! Using fertility trend data for now (!). Need to replace with mortality rate changes
    mortality['years'] = pl.array([1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030]) # Starting year bin
    mortality['trend'] = pl.array([194.3, 197.1, 202.9, 207.1, 207.1, 207.1, 207.1, 191.4, 177.1, 162.9, 150.0, 145.7, 142.9, 132.9, 125, 120, 115]) # Last 3 are projected!!
    mortality['trend'] /= mortality['trend'].mean()
    return mortality


# def default_age_year_fertility():
#     ''' From WPP2019_FERT_F07_AGE_SPECIFIC_FERTILITY.xlsx, filtered on Senegal '''
#     fertility = {}
#     fertility['ages'] = [0, 15, 20, 25, 30, 35, 40, 45, 50] # Starting age bin
#     fertility['years'] = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015], # Starting year bin
#     fertility['data'] = [
#         [0, 195.3,   297.1,   310.0,   260.9,   185.7,   78.1,    32.9, 0],
#         [0, 194.5,   296.1,   303.4,   262.7,   197.3,   92.5,    33.6, 0],
#         [0, 195.3,   299.0,   301.8,   267.6,   210.6,   110.4,   35.2, 0],
#         [0, 192.2,   300.5,   302.6,   270.9,   219.3,   126.8,   37.7, 0],
#         [0, 184.6,   296.6,   302.9,   270.6,   221.3,   134.5,   39.5, 0],
#         [0, 176.8,   292.8,   304.4,   273.3,   224.4,   137.4,   40.9, 0],
#         [0, 166.9,   289.2,   304.5,   278.8,   230.1,   138.6,   41.8, 0],
#         [0, 142.9,   263.8,   283.5,   264.0,   218.2,   129.4,   38.1, 0],
#         [0, 123.1,   241.6,   267.4,   250.9,   204.4,   119.3,   33.3, 0],
#         [0, 109.7,   222.7,   252.7,   236.9,   186.3,   104.5,   27.1, 0],
#         [0, 100.3,   207.8,   239.1,   222.8,   168.9,   89.4,    21.7, 0],
#         [0, 93.5,    202.7,   236.2,   218.9,   163.6,   84.6,    20.5, 0],
#         [0, 83.6,    195.2,   234.2,   214.1,   162.9,   87.4,    22.7, 0],
#         [0, 72.7,    180.2,   220.7,   200.0,   152.3,   82.1,    22.0, 0],
#         ]
#     return fertility


def default_age_fertility():
    ''' Less-developed countries, WPP2019_MORT_F15_3_LIFE_TABLE_SURVIVORS_FEMALE.xlsx, 1990-1995 '''
    f15 = 0.003 # Adjustment factor for women aged 15-20
    f20 = 0.25 # Adjustment factor for women aged 20-25
    fertility = {
            'bins': pl.array([ 0,  5, 10,      15,     20,     25,     30,     35,      40,       45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]), 
            'f':    pl.array([ 0,  0,  0, f15*0.0706, f20*0.0196, 0.0180, 0.0115, 0.00659, 0.00304, 0.00091,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0])}
    fertility['m'] = 0*fertility['f'] # Men don't have fertility -- probably could be handled differently!
    fertility['years'] = pl.array([1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030]) # Starting year bin
    fertility['trend'] = pl.array([194.3, 197.1, 202.9, 207.1, 207.1, 207.1, 207.1, 191.4, 177.1, 162.9, 150.0, 145.7, 142.9, 132.9, 125, 120, 115]) # Last 3 are projected!!
    fertility['trend'] /= fertility['trend'].mean()
    return fertility


def default_methods():
    methods = {}
    
    methods['map'] = {'None':0, 
                    'Lactation':1, 
                    'Implants':2, 
                    'Injectables':3, 
                    'IUDs':4, 
                    'Pill':5, 
                    'Condoms':6, 
                    'Other':7, 
                    'Traditional':8} # Add 'Novel'?
    methods['names'] = list(methods['map'].keys())
    
    methods['matrix'] = pl.array([
       [8.81230657e-01, 0.00000000e+00, 9.56761433e-04, 1.86518124e-03,        1.44017774e-04, 8.45978530e-04, 1.80273996e-04, 1.61138768e-05,        1.46032008e-04],
       [2.21565806e-05, 1.52074712e-04, 2.01423460e-06, 3.02135189e-06,        0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,        0.00000000e+00],
       [3.45441233e-04, 0.00000000e+00, 3.29206502e-02, 1.61138768e-05,        5.03558649e-06, 1.40996422e-05, 2.01423460e-06, 0.00000000e+00,        1.00711730e-06],
       [1.22767599e-03, 0.00000000e+00, 3.02135189e-05, 4.28810403e-02,        1.40996422e-05, 6.94910936e-05, 8.05693838e-06, 0.00000000e+00,        6.04270379e-06],
       [3.52491054e-05, 0.00000000e+00, 2.01423460e-06, 3.02135189e-06,        6.10715929e-03, 5.03558649e-06, 0.00000000e+00, 0.00000000e+00,        0.00000000e+00],
       [6.33476780e-04, 0.00000000e+00, 1.30925249e-05, 5.03558649e-05,        6.04270379e-06, 1.97092855e-02, 4.02846919e-06, 1.00711730e-06,        6.04270379e-06],
       [8.35907357e-05, 0.00000000e+00, 5.03558649e-06, 6.04270379e-06,        2.01423460e-06, 3.02135189e-06, 3.94689269e-03, 2.01423460e-06,        1.00711730e-06],
       [1.20854076e-05, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,        0.00000000e+00, 0.00000000e+00, 3.02135189e-06, 1.74432716e-03,        1.00711730e-06],
       [4.93487476e-05, 0.00000000e+00, 2.01423460e-06, 4.02846919e-06,        0.00000000e+00, 2.01423460e-06, 0.00000000e+00, 0.00000000e+00,        4.45145846e-03]])
    
    methods['matrix'][0,0] *= 0.53 # Correct for 2015
    
    methods['mcpr_years'] = pl.array([1986, 1992, 1997, 2005, 2010, 2012, 2014, 2015, 2016, 2017])
    
    mcpr_rates = pl.array([2.65, 4.53, 7.01, 7.62, 8.85, 11.3, 14.7, 15.3, 16.5, 18.8])
    mcpr_rates /= 100
    methods['mcpr_multipliers'] = (1-mcpr_rates)**4
    
    return methods


    
def default_efficacy():
    ''' From Guttmacher, fp/docs/gates_review/contraceptive-failure-rates-in-developing-world_1.pdf '''
    
    # Expressed as failure rates
    method_efficacy = sc.odict({
            "None":        0.0,
            "Lactation":   90.0,
            "Implants":    99.4,
            "Injectables": 98.3,
            "IUDs":        98.6,
            "Pill":        94.5,
            "Condoms":     94.6,
            "Other":       94.5,
            "Traditional": 86.6,
            })
    # method_efficacy[:] = 100 # To disable contraception
    
    method_efficacy = method_efficacy[:]/100
    
    # for key,value in method_efficacy.items():
    #     method_efficacy[key] = method_efficacy[key]/100
    
    # assert method_efficacy.keys() == default_methods() # Ensure ordering
    
    return method_efficacy


def default_barriers():
    barriers = sc.odict({
        'No need':45.6,
        'Opposition':30.1,
        'Knowledge':10.0,
        'Access':2.7,
        'Health':11.6,
        })
    barriers[:] /= barriers[:].sum() # Ensure it adds to 1    
    return barriers

def make_pars():
    pars = {}

    # Simulation parameters
    pars['name'] = 'Default' # Name of the simulation
    pars['n'] = int(1274*0.28*scale_factor) # Number of people in the simulation -- from Impact 2 / 1000
    pars['start_year'] = 1950
    pars['end_year'] = 2015
    pars['timestep'] = 3 # Timestep in months
    pars['verbose'] = True
    pars['seed'] = 1 # Random seed, if None, don't reset
    
    pars['methods'] = default_methods()
    pars['age_pyramid'] = default_age_pyramid()
    pars['age_mortality'] = default_age_mortality()
    pars['age_fertility'] = default_age_fertility()
    pars['method_efficacy'] = default_efficacy()
    pars['barriers'] = default_barriers()
    pars['mortality_factor'] = 3.0
    pars['fertility_factor'] = 40 # No idea why this needs to be so high
    pars['fertility_variation'] = [0.5,1.5] # Multiplicative range of fertility factors
    pars['method_age'] = 15 # When people start choosing a method (sexual debut)
    pars['max_age'] = 99
    pars['preg_dur'] = [9,9] # Duration of a pregnancy, in months
    
    
    return pars