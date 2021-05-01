"""
Расчет вероятности генерации вакансии
Реализовано два вида рассчета: с использованием предыдущего состояния существующих кислородных вакансий и без(wm/wom)
"""

import numpy as np
from modelling.const_variable import *
import math
import random
from numpy import unravel_index
from decimal import Decimal

class ProbabilityGeneration():
    """
    Класс рассчета вероятностей генерации/рекомбинации кислородных вакансий

    """
    def __init__(self):
        pass

    def calc_formattion_wm(self, massiv_field, massiv_temp, massive_for_check_vacancies):
        self.massive_for_check_vacancies = massive_for_check_vacancies
        self.massiv_probability_generation = np.zeros((SIZE_X, SIZE_Y))
        self.massiv_field = massiv_field
        self.massiv_temp = massiv_temp
        # print('temp: ', self.massiv_temp)

        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                print(FORMING_COEF_ENHANCEMENT * abs(self.massiv_field[self.i, self.j]))
                print('Напряженность поля в точке i=%s j=%s: %s' % (self.i, self.j, self.massiv_field[self.i, self.j]))
                print('Температура в точке i=%s j=%s: %s' % (self.i, self.j, self.massiv_temp[self.i, self.j]))
                if self.massive_for_check_vacancies[self.i, self.j] != 1:
                    self.massiv_probability_generation[self.i, self.j] = (
                        EFECTIVE_FREQ_VIBRATION * TIME_FORMATION_O_VAC * np.exp(
                            -(
                                    HEIGHT_MIGRATION_BARRIER - FORMING_COEF_ENHANCEMENT * abs(self.massiv_field[self.i, self.j])
                            ) /
                            (CONST_BOLTZMAN*self.massiv_temp[self.i, self.j])
                        )
                    )
                    print('Вероятность генерации i=%s j=%s: %s' % (self.i, self.j, self.massiv_probability_generation[self.i, self.j]))

        self.listOfCoordinates = []
        self.list_form_coord = []
        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                if self.massiv_probability_generation[self.i, self.j] >= POROG_GEN:
                    print('Создается вакансия; Вероятность:%s' % self.massiv_probability_generation[self.i, self.j])
                    self.massive_for_check_vacancies[self.i, self.j] = 1
                    self.list_form_coord.append([self.i, self.j])
        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                if self.massive_for_check_vacancies[self.i, self.j] == 1:
                    self.listOfCoordinates.append([self.i, self.j])
        print('Ячейки генерации:', self.list_form_coord)
        return self.listOfCoordinates

    def calc_formattion_wom(self, massiv_field, massiv_temp):
        self.massive_for_check_vacancies = np.zeros((SIZE_X, SIZE_Y))
        self.massiv_probability_generation = np.zeros((SIZE_X, SIZE_Y))
        self.massiv_field = massiv_field
        self.massiv_temp = massiv_temp

        return self.calc_formattion_wm(massiv_field=self.massiv_field, massive_for_check_vacancies=self.massive_for_check_vacancies, massiv_temp=self.massiv_temp)


    def calc_reset_wm(self, massiv_field, massiv_temp, massive_for_check_vacancies):
        self.massive_for_check_vacancies = massive_for_check_vacancies
        self.massiv_probability_generation = np.zeros((SIZE_X, SIZE_Y))
        self.massiv_field = massiv_field
        self.massiv_temp = massiv_temp

        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                if self.massive_for_check_vacancies[self.i, self.j] == 1:
                    print('Напряженность поля в точке i=%s j=%s: %s' % (self.i, self.j, self.massiv_field[self.i, self.j]))
                    print('Температура в точке i=%s j=%s: %s' % (self.i, self.j, self.massiv_temp[self.i, self.j]))
                    self.P_R0 = (
                            EFECTIVE_FREQ_VIBRATION * TIME_FORMATION_O_VAC * math.exp(-HEIGHT_MIGRATION_BARRIER /
                        (CONST_BOLTZMAN * self.massiv_temp[self.i, self.j])
                    )
                    )
                    self.v = (LATTICE_CONST / EFECTIVE_FREQ_VIBRATION) * math.exp(-HEIGHT_MIGRATION_BARRIER /
                        (CONST_BOLTZMAN * self.massiv_temp[self.i, self.j]))\
                        * math.sinh(
                            (CHARGE_E * DRIFT_COEF * abs(self.massiv_field[self.i, self.j]))
                            / (CONST_BOLTZMAN * self.massiv_temp[self.i, self.j])
                        )
                    self.u = 0.5
                    self.beta = RECOMBINATION_ENHANCEMENT_FACTOR * math.exp((-self.v*TIME_FORMATION_O_VAC)/CONCENTRATION_DECAYING_LENGHT_IONS) * self.u
                    print("P_R0:", self.P_R0)
                    print("v:", self.v)
                    print("beta:", self.beta)

                    self.P_R = self.P_R0 * self.beta
                    self.massiv_probability_generation[self.i, self.j] = self.P_R
                    print('Вероятность рекомбинации i=%s j=%s: %s' % (self.i, self.j, self.massiv_probability_generation[self.i, self.j]))

        self.listOfCoordinates = []
        self.list_rec_coordinates = []
        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                if self.massiv_probability_generation[self.i, self.j] >= POROG_REC:
                    self.massive_for_check_vacancies[self.i, self.j] = 0
                    self.list_rec_coordinates.append([self.i, self.j])
        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                if self.massive_for_check_vacancies[self.i, self.j] == 1:
                    self.listOfCoordinates.append([self.i, self.j])

        print('Ячейки рекомбинации:', self.list_rec_coordinates)
        return self.listOfCoordinates