#! /usr/bin/env python
import os

os.environ['MPLBACKEND'] = 'Agg'
os.environ['PYMT_DEBUG'] = '1'

os.mkdir('_testing')
os.chdir('_testing')

from pymt.components import Sedflux3D as Model

model = Model()
config_file, config_dir = model.setup('.')
model.initialize(config_file, dir=config_dir)
print(model.as_yaml())

for default in model.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1][0], units=default[1][1]))
