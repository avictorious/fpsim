'''
Simple script to run analyses using the heavy-lifting CalObj class.
'''

import os
import pylab as pl
import fp_utils as fpu
import sciris as sc

# Comment/uncomment these to run different analyses
torun = [
        #'loadsave',
        'plot_matrix',
        #'plot_slice',
        ]

filename = 'data/nigeria_cal.obj' # Generated by e.g. sc.saveobj('nigeria_cal.obj', calobj.cal)


sc.tic()


# Nigeria 2013 DHS
username = os.path.split(os.path.expanduser('~'))[-1]
filedict = {'dklein': os.path.join( os.getenv("HOME"), 'Dropbox (IDM)', 'FP Dynamic Modeling', 'DHS', 'Country data', 'Nigeria', '2013', 'NGIR6ADT', 'NGIR6AFL.DTA'),
              'cliffk': '/u/cliffk/idm/fp/data/DHS/NGIR6ADT/NGIR6AFL.DTA',
             }

cache = os.path.join('data', 'nigeria.cal')

try:
    filename = filedict[username]
except:
    raise Exception(f'User {username} not found among users {list(filedict.keys())}, cannot find data.')

def load_from_file():
    print(f'Loading calobj from file {filename}')
    calobj = fpu.CalObj(filename) # Create from saved data
    print(f'Saving to cache {cache}')
    calobj.save(cache)

    return calobj


if os.path.isfile(cache):
    try:
        print('Trying to load from cache {cache}...')
        calobj = fpu.CalObj(cache) # Load saved object
        print('Loaded presaved object...')
    except:
        print(f'Unable to load from cache {cache}, falling back to loading from file {filename}')
        calobj = load_from_file()
else:
    calobj = load_from_file()

if 'plot_matrix' in torun:
    calobj.plot_transitions()


if 'plot_slice' in torun:
    calobj.plot_slice(key='None')


sc.toc()
print('Done')

pl.show()
