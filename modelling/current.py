"""
Рассчет тока на основе полученных данных электроформовки
"""
from modelling.const_variable import *
import math

class Current:
    def __init__(self):
        pass

    def calc_density_current(self, massive_field, massive_for_check_vacancies, massive_temp):
        # print('massive_field:', massive_field)
        # print('massive_temp:', massive_temp)
        self.density_current = 0
        for self.i in range(0, SIZE_X):
            # считаем среднюю напряженность в столбце
            self.E = 0
            for self.j in range(0, SIZE_Y):
                self.E += massive_field[self.i, self.j]
            self.E = self.E / SIZE_Y
            print('Средняя напряженность в столбце:', self.E)

            # считаем среднюю температуру в столбце
            self.T = 0
            for self.j in range(0, SIZE_Y):
                self.T += massive_temp[self.i, self.j]
            self.T = self.T / SIZE_Y
            print('Средняя температура в столбце:', self.T)

            self.one_density_current = abs(self.E) * math.exp(
                (A_CONST*(math.sqrt(abs(self.E))/self.T)) - B_CONST
            )
            if self.one_density_current > CURRENT_OGR:
                self.density_current += CURRENT_OGR
            else:
                self.density_current += self.one_density_current

        print("current:", self.density_current)
        return abs(self.density_current)
