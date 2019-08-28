'''
Simple script to run analyses using the heavy-lifting CalObj class.
'''

import calobj as co
import sciris as sc

# Comment/uncomment these to run different analyses
torun = [
#        'loadsave',
        'plot',
        ]

filename = 'data/nigeria_cal.obj'


sc.tic()


if 'loadsave' in torun:
    print('Loading original data and saving...')
    filename = '/u/cliffk/idm/fp/data/DHS/NGIR6ADT/NGIR6AFL.DTA' # Nigeria 2013 DHS -- warning, system-specific!
    calobj = co.CalObj(filename)
    calobj.save('data/nigeria_cal.obj')
else:
    print('Loading presaved object...')
    #calobj = co.load(filename) # Load saved object
    calobj = co.CalObj(filename) # Create from saved data
   

if 'plot' in torun:
    calobj.plot_transitions()
    

sc.toc()
print('Done')