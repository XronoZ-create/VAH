"""
Тест формовки с памятью формировавшихся ячеек
"""

from modelling.distribution_electric_field import DistributionElectricPotential, DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration
from draw.draw_set_reset import DrawSetReset
from modelling.probability import ProbabilityGeneration
from modelling.current import Current
import copy
import numpy as np
from modelling.const_variable import *
import matplotlib.pyplot as plt
import time

draw_set_reset = DrawSetReset(num_plots=3)
d = DistributionElectricPotential()
dt = DistributionTempInVolume()
df = DistributionElectricField()
probgen = ProbabilityGeneration()
current = Current()

massive_for_check_vacancies = np.zeros((SIZE_X, SIZE_Y))
for U_ in range(40,200,10):
    print('U:', U_ / 10)
    d.calc_wm(POTENTIAL_O_VAC=U_/10, massive_for_check_vacancies=massive_for_check_vacancies)
    dt.calc_wm(massive_for_check_vacancies=massive_for_check_vacancies)

    massiv_field = df.calc_wm(massiv_potential=d.massiv_potential)
    coord_o_vac = probgen.calc_formattion_wm(
        massiv_temp=dt.massiv_temp,
        massiv_field=massiv_field,
        massive_for_check_vacancies=massive_for_check_vacancies
    )
    massive_for_check_vacancies = probgen.massive_for_check_vacancies
    d.calc_wm(POTENTIAL_O_VAC=U_/10, massive_for_check_vacancies=probgen.massive_for_check_vacancies)
    dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)


    draw_set_reset.draw_vacancies(coord_o_vac, legend=U_/10)
    draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
    draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
    draw_set_reset.snap()

draw_set_reset.create_animation()
plt.show()



