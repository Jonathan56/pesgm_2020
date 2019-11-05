from tqdm import tqdm
from datetime import datetime, timedelta
import pandas
import numpy
from optimization import maximize_self_consumption


df = pandas.read_csv('results/5min_houses_pv_052014_052015_v0001.csv',
                     parse_dates=[0], index_col=[0])

# normalize pv data [0, 1]
df['pv_coef'] = df['pv_w/m2'] / 1000

# pick a PV size, and calculate PV production
installed_pv_kW = 40
df['pv_kW'] = df['pv_coef'] * installed_pv_kW

# Select houses with larger energy consumption
nb_houses = 'all'
tmp = df[[k for k in df.columns if 'dish'
          not in k and 'houses' not in k
          and 'pv' not in k and 'self' not in k]]
houses_with_battery = (tmp.sum() * 5 / 60).sort_values(ascending=False).index.tolist()
print('Houses with batteries: ')
print(houses_with_battery)
print('')

# Start simulation
start = datetime.now()
battery_sizes = list(numpy.linspace(0.25, 10, 10*4))
battery_kW = 2  # kW
large_glpk = {key:None for key in battery_sizes}
periods = pandas.date_range(start='2014-05-01 00:00:00',
                            end='2015-04-30 23:55:00', periods=40).round('5T')

for batt_size in battery_sizes:
    print('Battery size: ' + str(batt_size) + ' kWh')
    df_glpk = pandas.DataFrame()
    for index in tqdm(range(0, len(periods[:-1])), desc='Progress'):
        # Uncontrollable demand
        uncontrollable = df.copy()
        uncontrollable = uncontrollable.loc[periods[index]:periods[index+1], :]
        uncontrollable['p'] = uncontrollable['houses_kW'] - uncontrollable['pv_kW']
        uncontrollable['index'] = list(range(0, len(uncontrollable)))
        uncontrollable.set_index('index', inplace=True)
        uncontrollable = uncontrollable[['p']]

        # Order book for Shapeable
        data = {'startby': [],
                'endby': [],
                'max_kw': [],
                'end_kwh': []}
        dfshapeables = pandas.DataFrame(data=data)


        # Order book for Deferrable
        data = {'startby': [],
                'endby': [],
                'duration': [],
                'profile_kw': []}
        dfdeferrables = pandas.DataFrame(data=data)

        # Order book for battery
        data = {'startby': [0] * len(houses_with_battery),
                'endby': [len(uncontrollable)] * len(houses_with_battery),
                'min_kw': [battery_kW] * len(houses_with_battery),
                'max_kw': [battery_kW] * len(houses_with_battery),
                'max_kwh': [batt_size] * len(houses_with_battery),
                'initial_kwh': [batt_size/2] * len(houses_with_battery),
                'end_kwh': [batt_size/2] * len(houses_with_battery),
                'eta': [0.95] * len(houses_with_battery)}
        dfbatteries = pandas.DataFrame(data=data)

        # Run optimization
        glpk = maximize_self_consumption(uncontrollable, dfbatteries,
                                  dfshapeables, dfdeferrables,
                                  timestep=5/60, solver='glpk',
                                  solver_path=None, verbose=False)

        # Save results
        tmp = pandas.DataFrame(
                index=df.loc[periods[index]:periods[index+1], :].index,
                data={'battery_kW': glpk['demand_controllable']})
        df_glpk = pandas.concat([df_glpk, tmp], axis=0)

    # Save results to check later
    large_glpk[batt_size] = df_glpk.copy()

print('Time elapsed (hh:mm:ss.ms) {}'.format(
    datetime.now() - start))

import pickle
with open('results/glpk_batterykWh_' + str(battery_kW) + 'kW_pv=' + str(installed_pv_kW)+ 'kW_nbhouse=' + str(nb_houses) + '.obj', 'wb') as fp:
    pickle.dump(large_glpk, fp)
