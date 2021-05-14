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


@logger.catch
def start():
    draw_set_reset = DrawSetReset(num_plots=4)
    d = DistributionElectricPotential()
    dt = DistributionTempInVolume()
    df = DistributionElectricField()
    probgen = ProbabilityGeneration()
    current = Current()
    dv = DrawVAH()

    # Формовка 1 в значениях близких к нулю
    for _U in range(SMALL_STEP_FOR_ZERO, STEP_U_FORM, SMALL_STEP_FOR_ZERO):
        print('U:', _U / 1000)

        if _U == SMALL_STEP_FOR_ZERO:
            d.calc_wom(POTENTIAL_O_VAC=_U / 1000)
            dt.calc_wom()

            coord_o_vac = probgen.generate_random_vac()
        else:
            coord_o_vac = probgen.calc_formattion_wm(
                massiv_temp=dt.massiv_temp,
                massiv_field=massiv_field,
                massive_for_check_vacancies=probgen.massive_for_check_vacancies
            )

        d.calc_wm(POTENTIAL_O_VAC=_U / 1000, massive_for_check_vacancies=probgen.massive_for_check_vacancies, massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies, POTENTIAL_O_VAC=_U / 1000)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                    massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                    massive_temp=dt.massiv_temp
                                                                                    )
                       )

    # Формовка 1
    for _U in range(STEP_U_FORM, MAX_U_FORM+STEP_U_FORM, STEP_U_FORM):
        print('U:', _U / 1000)

        coord_o_vac = probgen.calc_formattion_wm(
            massiv_temp=dt.massiv_temp,
            massiv_field=massiv_field,
            massive_for_check_vacancies=probgen.massive_for_check_vacancies
        )

        d.calc_wm(POTENTIAL_O_VAC=_U / 1000, massive_for_check_vacancies=probgen.massive_for_check_vacancies, massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies, POTENTIAL_O_VAC=_U / 1000)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                    massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                    massive_temp=dt.massiv_temp
                                                                                    )
                       )

    # Формовка 2
    for _U in range(MAX_U_FORM, START_U_FORM, -STEP_U_FORM):
        print('U:', _U / 1000)
        coord_o_vac = probgen.calc_formattion_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field, massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()

        d.calc_wm(POTENTIAL_O_VAC=(_U / 1000), massive_for_check_vacancies=probgen.massive_for_check_vacancies, massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies, POTENTIAL_O_VAC=_U / 1000)
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                   massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                   massive_temp=dt.massiv_temp
                                                                                   )
                       )

    # Формовка 2 в значениях близких к нулю
    for _U in range(START_U_FORM+STEP_U_FORM, START_U_FORM-SMALL_STEP_FOR_ZERO, -SMALL_STEP_FOR_ZERO):
        print('U:', _U / 1000)
        coord_o_vac = probgen.calc_formattion_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field, massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()

        d.calc_wm(POTENTIAL_O_VAC=(_U / 1000), massive_for_check_vacancies=probgen.massive_for_check_vacancies, massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies, POTENTIAL_O_VAC=_U / 1000)
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                   massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                   massive_temp=dt.massiv_temp
                                                                                   )
                       )


    # Рекомбинация 1 в значениях близких к нулю
    for _U in range(START_U_FORM - SMALL_STEP_FOR_ZERO, START_U_FORM - STEP_U_FORM, -SMALL_STEP_FOR_ZERO):
        print('U:', _U / 1000)

        coord_o_vac = probgen.calc_reset_wm(
            massiv_temp=dt.massiv_temp,
            massiv_field=massiv_field,
            massive_for_check_vacancies=probgen.massive_for_check_vacancies
        )

        d.calc_wm(POTENTIAL_O_VAC=_U / 1000, massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                  massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                               POTENTIAL_O_VAC=_U / 1000)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                     massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                     massive_temp=dt.massiv_temp
                                                                                     )
                       )

    # Рекомбинация 1
    for _U in range(START_U_FORM - STEP_U_FORM, -(MAX_U_FORM + STEP_U_FORM), -STEP_U_FORM):
        print('U:', _U / 1000)

        coord_o_vac = probgen.calc_reset_wm(
            massiv_temp=dt.massiv_temp,
            massiv_field=massiv_field,
            massive_for_check_vacancies=probgen.massive_for_check_vacancies
        )

        d.calc_wm(POTENTIAL_O_VAC=_U / 1000, massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                  massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                               POTENTIAL_O_VAC=_U / 1000)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                     massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                     massive_temp=dt.massiv_temp
                                                                                     )
                       )

    # Рекомбинация 2
    for _U in range(-MAX_U_FORM, START_U_FORM, STEP_U_FORM):
        print('U:', _U / 1000)
        coord_o_vac = probgen.calc_reset_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field,
                                            massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()

        d.calc_wm(POTENTIAL_O_VAC=(_U / 1000), massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                  massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                               POTENTIAL_O_VAC=_U / 1000)
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                     massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                     massive_temp=dt.massiv_temp
                                                                                     )
                       )

    # Рекомбинация 2 в значениях близких к нулю
    for _U in range(START_U_FORM-STEP_U_FORM, START_U_FORM + SMALL_STEP_FOR_ZERO, SMALL_STEP_FOR_ZERO):
        print('U:', _U / 1000)
        coord_o_vac = probgen.calc_reset_wm(massiv_temp=dt.massiv_temp, massiv_field=massiv_field,
                                            massive_for_check_vacancies=probgen.massive_for_check_vacancies)

        draw_set_reset.draw_vacancies(coord_o_vac, legend=_U / 1000)
        draw_set_reset.draw_temp_distribution(massive_temp=dt.massiv_temp)
        draw_set_reset.draw_electric_field_distribution(massive_field=df.massiv_field)
        draw_set_reset.draw_potential_distribution(potential=d.massiv_potential)
        draw_set_reset.snap()

        d.calc_wm(POTENTIAL_O_VAC=(_U / 1000), massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                  massiv_potential=d.massiv_potential)
        dt.calc_wm(massive_for_check_vacancies=probgen.massive_for_check_vacancies)
        massiv_field = df.calc(massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                               POTENTIAL_O_VAC=_U / 1000)
        dv.add_point_1(potencial=_U / 1000, current=current.calc_density_current_hrs(massive_field=massiv_field,
                                                                                     massive_for_check_vacancies=probgen.massive_for_check_vacancies,
                                                                                     massive_temp=dt.massiv_temp
                                                                                     )
                       )

    draw_set_reset.create_animation()
    plt.show()
    dv.draw()


start()