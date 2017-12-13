#! /usr/bin/env python
import os

os.environ['MPLBACKEND'] = 'Agg'
os.environ['PYMT_DEBUG'] = '1'

os.mkdir('_testing')
os.chdir('_testing')

from pymt.components import Sedflux3D as Model

model = Model()
model.setup('.')
model.initialize('sedflux_3d_init.kvf')
print(model.as_yaml())

for default in model.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1][0], units=default[1][1]))
