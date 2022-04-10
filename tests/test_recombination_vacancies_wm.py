from modelling.distribution_electric_field import DistributionElectricPotential, DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration
from draw.draw_set_reset import DrawVacancies
from modelling.probability import ProbabilityGeneration
from modelling.current import Current
import copy
import matplotlib.pyplot as plt
from loguru import logger

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")

@logger.catch
def start():
    draw_vac = DrawVacancies()
    d = DistributionElectricPotential()
    dt = DistributionTempInVolume()
    df = DistributionElectricField()
    probgen = ProbabilityGeneration()
    current = Current()

    U_FORM = 30

    # Формовка
    d.calc_wm(POTENTIAL_O_VAC=U_FORM)
    dt.calc_wm()
    massiv_field = df.calc_wm(massiv_potential=d.massiv_potential)
    coord_o_vac = probgen.calc_formattion_wom(massiv_temp=dt.massiv_temp, massiv_field=massiv_field)
    draw_vac.draw(coord_o_vac, legend=str(U_FORM/10))

    copy_massive_for_check_vacancies = copy.deepcopy(probgen.massive_for_check_vacancies)

    # Рекомбинация
    for _U in range(U_FORM, 0, -1):
        d.calc_wm(POTENTIAL_O_VAC=(_U/10), massive_for_check_vacancies=copy_massive_for_check_vacancies)
        dt.calc_wm(massive_for_check_vacancies=copy_massive_for_check_vacancies)
        massiv_field = df.calc_wm(massiv_potential=d.massiv_potential)
        coord_o_vac = probgen.calc_reset_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field, massive_for_check_vacancies=copy_massive_for_check_vacancies)
        draw_vac.draw(coord_o_vac, legend=str(_U/10))

    draw_vac.create_animation()
    plt.show()

start()