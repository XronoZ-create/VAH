from modelling.distribution_electric_field import DistributionElectricPotential, DistributionElectricField
from modelling.distribution_temp_in_volume import DistributionTempInVolume
from modelling.time_generation import TimeGeneration
from draw.draw_set_reset import DrawSetReset
from modelling.probability_generation import ProbabilityGeneration
from modelling.current import Current
import copy
import matplotlib.pyplot as plt
from loguru import logger
from modelling.const_variable import *
from draw.draw_VAH import DrawVAH


logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")
MAX_U_FORM = 60

@logger.catch
def start():
    draw_set_reset = DrawSetReset(num_plots=3)
    d = DistributionElectricPotential()
    dt = DistributionTempInVolume()
    df = DistributionElectricField()
    probgen = ProbabilityGeneration()
    current = Current()
    dv = DrawVAH()

    # Формовка
    for _U in range(0, MAX_U_FORM, 1):
        print('U:', _U / 10)

        # d.calc_wom(POTENTIAL_O_VAC=_U / 10)
        # dt.calc_wom()
        if _U != 0:
            d.calc_wm(POTENTIAL_O_VAC=_U / 10, massive_for_check_vacancies=probgen.massive_for_check_vacancies)
            dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        else:
            d.calc_wom(POTENTIAL_O_VAC=_U / 10)
            dt.calc_wom()
        massiv_field = df.calc(massiv_potential=d.massiv_potential)
        if _U != 0:
            coord_o_vac = probgen.calc_formattion_wm(
                massiv_temp=dt.massiv_temp,
                massiv_field=massiv_field,
                massive_for_check_vacancies=probgen.massive_for_check_vacancies
            )
        else:
            coord_o_vac = probgen.calc_formattion_wom(
                massiv_temp=dt.massiv_temp,
                massiv_field=massiv_field
            )

        d.calc_wm(POTENTIAL_O_VAC=_U / 10, massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 10)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.snap()
        dv.add_point_1(potencial=_U / 10, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                    massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                    massive_temp=dt.massiv_temp
                                                                                    )
                       )

    # Рекомбинация
    for _U in range(MAX_U_FORM, 0, -1):
        print('U:', _U / 10)
        coord_o_vac = probgen.calc_reset_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field, massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 10)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.snap()

        d.calc_wm(POTENTIAL_O_VAC=(_U / 10), massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massiv_potential=d.massiv_potential)
        dv.add_point_1(potencial=_U / 10, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                   massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                   massive_temp=dt.massiv_temp
                                                                                   )
                       )

    # ЛЕВАЯ ЧАСТЬ
    # Формовка
    for _U in range(0, -MAX_U_FORM, -1):
        print('U:', _U / 10)

        # d.calc_wom(POTENTIAL_O_VAC=_U / 10)
        # dt.calc_wom()
        if _U != 0:
            d.calc_wm(POTENTIAL_O_VAC=_U / 10, massive_for_check_vacancies=probgen.massive_for_check_vacancies)
            dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        else:
            d.calc_wom(POTENTIAL_O_VAC=_U / 10)
            dt.calc_wom()
        massiv_field = df.calc(massiv_potential=d.massiv_potential)
        if _U != 0:
            coord_o_vac = probgen.calc_formattion_wm(
                massiv_temp=dt.massiv_temp,
                massiv_field=massiv_field,
                massive_for_check_vacancies=probgen.massive_for_check_vacancies
            )
        else:
            coord_o_vac = probgen.calc_formattion_wom(
                massiv_temp=dt.massiv_temp,
                massiv_field=massiv_field
            )

        d.calc_wm(POTENTIAL_O_VAC=_U / 10, massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 10)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.snap()
        dv.add_point_1(potencial=_U / 10, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                   massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                   massive_temp=dt.massiv_temp
                                                                                   )
                       )

    # Рекомбинация
    for _U in range(-MAX_U_FORM, 0, 1):
        print('U:', _U / 10)
        coord_o_vac = probgen.calc_reset_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field,
                                            massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 10)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.snap()

        d.calc_wm(POTENTIAL_O_VAC=(_U / 10), massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massiv_potential=d.massiv_potential)
        dv.add_point_1(potencial=_U / 10, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                   massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                   massive_temp=dt.massiv_temp
                                                                                   )
                       )

    draw_set_reset.create_animation()
    plt.show()
    dv.draw()

start()