"""
Тест формовки без памяти сформировавшихся ячеек
"""

from modelling.distribution_electric_field import DistributionElectricPotential, DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration
from draw.draw_set_reset import DrawVacancies
from modelling.probability_generation import ProbabilityGeneration
from modelling.current import Current
import copy
import numpy as np
from modelling.const_variable import *
import matplotlib.pyplot as plt
import time

draw_vac = DrawVacancies()
d = DistributionElectricPotential()
dt = DistributionTempInVolume()
df = DistributionElectricField()
probgen = ProbabilityGeneration()
current = Current()

for U_ in range(200, 700, 10):
    d.calc_wom(POTENTIAL_O_VAC=U_/100)
    dt.calc_wom()

    massiv_field = df.calc(massiv_potential=d.massiv_potential)
    coord_o_vac = probgen.calc_formattion_wom(
        massiv_temp=dt.massiv_temp,
        massiv_field=massiv_field
        )
    # massive_for_check_vacancies = probgen.massive_for_check_vacancies


    draw_vac.draw(coord_o_vac, legend=U_/100)
draw_vac.create_animation()
plt.show()



