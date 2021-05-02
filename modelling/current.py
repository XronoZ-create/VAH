"""
Рассчет тока на основе полученных данных электроформовки
"""
from modelling.const_variable import *
import math

class Current:
    def __init__(self):
        pass

    def calc_density_current_hrs(self, massive_field, massive_for_check_vacancies, massive_temp):
        # print('massive_field:', massive_field)
        # print('massive_temp:', massive_temp)
        self.density_current = 0
        for self.i in range(0, SIZE_X):
            # Считаем среднее расстояние между ловушками
            self.list_vac_in_row = []
            for self.j in range(0, SIZE_Y):
                if massive_for_check_vacancies[self.i, self.j] == 1:
                    self.list_vac_in_row.append(self.j)
            if len(self.list_vac_in_row) > 0:
                self.all_space = 0
                self.i_space = 0
                for self.vac in self.list_vac_in_row:
                        self.all_space += self.vac * MIDDLE_SPACE_TRAP
                        self.i_space += 1
                self.s = MIDDLE_SPACE_TRAP + (((SIZE_Y - self.i_space) * MIDDLE_SPACE_TRAP) / SIZE_Y)
                print('middle space:', self.s)

            # считаем среднюю напряженность в столбце
            self.E = 0
            for self.j in range(0, SIZE_Y):
                self.E += massive_field[self.i, self.j]
            self.E = self.E / SIZE_Y

            # считаем среднюю температуру в столбце
            self.T = 0
            for self.j in range(0, SIZE_Y):
                self.T += massive_temp[self.i, self.j]
            self.T = self.T / SIZE_Y

            if len(self.list_vac_in_row) > 0:
                print('other:', (CHARGE_E / (self.s ** 2)) * (ENERGY_IONIZATION_TRAP / CONST_PLANKA))
                print('exp:', math.exp(-
                        (
                                ENERGY_IONIZATION_TRAP - (CONST_FRENKEL * math.sqrt(abs(self.E)))
                        ) / (
                                CONST_BOLTZMAN * self.T
                        )
                    ))
                print('tanh:', math.tanh(
                        (
                                (CHARGE_E * abs(self.E) * self.s) /
                                (2 * CONST_BOLTZMAN * self.T)
                        )
                    ))
                print('F:', self.E)
                self.one_density_current = (CHARGE_E / (self.s ** 2)) * (ENERGY_IONIZATION_TRAP / CONST_PLANKA) * \
                    math.exp(-
                        (
                                ENERGY_IONIZATION_TRAP - (CONST_FRENKEL * math.sqrt(abs(self.E)) )
                        ) / (
                                CONST_BOLTZMAN * self.T
                        )
                    ) * math.tanh(
                        (
                                (CHARGE_E * abs(self.E) * self.s) /
                                (2 * CONST_BOLTZMAN * self.T)
                        )
                    )
                if self.one_density_current > CURRENT_OGR:
                    self.density_current += CURRENT_OGR
                else:
                    self.density_current += self.one_density_current
            else:
                self.density_current += ZERRO_CURRENT

        print("current:", self.density_current)
        return self.density_current
