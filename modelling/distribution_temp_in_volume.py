#Расчет распределения температуры в обьеме оксидной пленки
#Реализовано два вида рассчета: с использованием предыдущего состояния существующих кислородных вакансий и без(wm/wom)

import numpy as np
from modelling.const_variable import *
import random

class DistributionTempInVolume():
    def __init__(self):
        pass

    def calc_wm(self, massive_for_check_vacancies):
        self.massiv_temp = np.zeros((SIZE_X, SIZE_Y))
        self.massive_for_check_vacancies = massive_for_check_vacancies
        self.massive_help_for_temp = np.zeros((SIZE_X, SIZE_Y))

        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                self.massiv_temp[self.i, self.j] = TEMP_ENVIRONMENT
                
        for self.iter_cycleTemp in range(0, 100):
            for self.i in range(0, SIZE_X):
                for self.j in range(0, SIZE_Y):
                    if self.i == SIZE_X-1:
                        self.t1 = TEMP_ENVIRONMENT
                    else:
                        self.t1 = self.massiv_temp[self.i+1, self.j]

                    if self.i == 0:
                        self.t2 = TEMP_ENVIRONMENT
                    else:
                        self.t2 = self.massiv_temp[self.i-1, self.j]

                    if self.j == SIZE_Y-1:
                        self.t3 = TEMP_ENVIRONMENT
                    else:
                        self.t3 = self.massiv_temp[self.i, self.j+1]

                    if self.j == 0:
                        self.t4 = TEMP_ENVIRONMENT
                    else:
                        self.t4 = self.massiv_temp[self.i, self.j-1]

                    self.q = 0
                    if self.massive_for_check_vacancies[self.i, self.j] == 1:
                        self.massive_help_for_temp[self.i, self.j] = TEMP_O_VAC+(random.randint(-STEP_FRIX_TEMP, STEP_FRIX_TEMP))
                    else:
                        self.massive_help_for_temp[self.i, self.j] = (
                                self.massiv_temp[self.i, self.j] +
                                (self.t1 - 2 * self.massiv_temp[self.i, self.j] + self.t2) * dt / (h * h) +
                                (self.t3 - 2 * self.massiv_temp[self.i, self.j] + self.t4) * dt / (h * h)
                        )

            for self.i in range(0, SIZE_X):
                for self.j in range(0, SIZE_Y):
                        self.massiv_temp[self.i, self.j] = self.massive_help_for_temp[self.i, self.j]

    def calc_wom(self):
        self.massive_for_check_vacancies = np.zeros((SIZE_X, SIZE_Y))
        self.calc_wm(massive_for_check_vacancies=self.massive_for_check_vacancies)