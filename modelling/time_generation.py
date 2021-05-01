# Расчет скорости генерации вакансии
import numpy as np
from modelling.const_variable import *
import math
import random
from numpy import unravel_index

class TimeGeneration():
    def __init__(self):
        self.massiv_time_generation = np.zeros( (SIZE_X, SIZE_Y) )
        self.massive_for_check_vacancies = np.zeros( (SIZE_X, SIZE_Y) )
    def calc(self, massiv_potential, massiv_temp):
        self.massiv_potential = massiv_potential
        self.massiv_temp = massiv_temp
        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):
                    self.massiv_time_generation[self.i, self.j] = (
                        -1/(EFECTIVE_FREQ_VIBRATION * math.exp(
                            -(
                                (ENERGY_FORMATION_O_VAC-COEF_COMMUNICATION_POLAR*abs(
                                    0.01*self.massiv_potential[self.i, self.j])
                                ) * CHARGE_E
                            )/(
                                CONST_BOLTZMAN*self.massiv_temp[self.i, self.j]
                            )
                        )

                    )
                    ) * math.log(random.random())

    def get_min_value(self):
        self.nmin = np.where(self.massiv_time_generation == np.amin(self.massiv_time_generation))
        print(np.amin(self.massiv_time_generation))
        self.listOfCoordinates = list(zip(self.nmin[0], self.nmin[1]))
        print(self.listOfCoordinates)

        for self.i in self.listOfCoordinates:
            self.massive_for_check_vacancies[self.i] = 1
        return self.listOfCoordinates
