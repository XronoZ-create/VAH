"""
Тест формовки при одном заданном напряжение
"""

from modelling.distribution_electric_field import DistributionElectricPotential, DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration
from draw.draw_set_reset import DrawVacancies
from modelling.probability import ProbabilityGeneration
from modelling.current import Current
import copy
import matplotlib.pyplot as plt


draw_vac = DrawVacancies()
d = DistributionElectricPotential()
dt = DistributionTempInVolume()
df = DistributionElectricField()
probgen = ProbabilityGeneration()
current = Current()

d.calc(POTENTIAL_O_VAC=3)
dt.calc()
massiv_field = df.calc_wm(massiv_potential=d.massiv_potential)
coord_o_vac = probgen.calc_formattion_wom(massiv_temp=dt.massiv_temp, massiv_field=massiv_field)
draw_vac.draw(coord_o_vac)
plt.show()
copy_massive_for_check_vacancies = copy.deepcopy(probgen.massive_for_check_vacancies)
