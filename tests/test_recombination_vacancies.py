from modelling.distribution_electric_field import DistributionElectricPotential, DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration
from draw.draw_set_reset import DrawVacancies
from modelling.probability_generation import ProbabilityGeneration
from modelling.current import Current
import copy
import matplotlib.pyplot as plt

draw_vac = DrawVacancies()
d = DistributionElectricPotential()
dt = DistributionTempInVolume()
df = DistributionElectricField()
probgen = ProbabilityGeneration()
current = Current()

U_FORM = 3
U_REC = 2

# Формовка
d.calc(POTENTIAL_O_VAC=U_FORM)
dt.calc()
massiv_field = df.calc(massiv_potential=d.massiv_potential)
coord_o_vac = probgen.calc_formattion_wom(massiv_temp=dt.massiv_temp, massiv_field=massiv_field)
draw_vac.draw(coord_o_vac)
copy_massive_for_check_vacancies = copy.deepcopy(probgen.massive_for_check_vacancies)

# Рекомбинация
d.calc(POTENTIAL_O_VAC=U_REC, massive_for_check_vacancies=copy_massive_for_check_vacancies)
dt.calc(massive_for_check_vacancies=copy_massive_for_check_vacancies)
massiv_field = df.calc(massiv_potential=d.massiv_potential)
coord_o_vac = probgen.calc_reset_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field, massive_for_check_vacancies=copy_massive_for_check_vacancies)
draw_vac.draw(coord_o_vac)

draw_vac.create_animation()
plt.show()