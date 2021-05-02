# Первый этап моделирования. Расчет расперделения электрического поля в обьеме оксидной пленки
import numpy as np
from modelling.const_variable import *
from contextlib import suppress
import math

class DistributionElectricPotential():
    def __init__(self):
        pass

    def calc_wm(self, POTENTIAL_O_VAC, massive_for_check_vacancies, massiv_potential):
        """
        Рассчет потенциалов для 2-х мерного случая

        :return:
        """
        """
        Заполняем массив около пластин
        """
        self.massiv_potential = massiv_potential
        self.massive_for_check_vacancies = massive_for_check_vacancies

        for self.iter_cycleTemp in range(0, 100):

            for self.i in range(0, SIZE_X):
                for self.j in range(0, SIZE_Y):
                    if self.massive_for_check_vacancies[self.i, self.j] == 1:
                        self.massiv_potential[self.i, self.j] = POTENTIAL_O_VAC

            for self.i in range(0, SIZE_X):
                    self.Zcol = 0
                    while self.massive_for_check_vacancies[self.i, self.Zcol] == 1:
                        if self.Zcol == SIZE_Y-1:
                            break
                        self.Zcol += 1
                    self.massiv_potential[self.i, SIZE_Y-1] = 0
                    if self.Zcol != 0:
                        self.massiv_potential[self.i, self.Zcol] = POTENTIAL_O_VAC
                    elif self.Zcol == 0 and self.i == 15:
                        self.massiv_potential[self.i, self.Zcol] = POTENTIAL_O_VAC
                    self.Zcol = 0

            # for self.j in range(1, SIZE_Y-1):
            #     for self.i in range(0, SIZE_X):
            #         if self.i == 0:
            #             self.massiv_potential[0, self.j] = self.massiv_potential[1, self.j]
            #             continue
            #         if self.i == SIZE_X-1:
            #             self.massiv_potential[SIZE_X-1, self.j] = self.massiv_potential[SIZE_X-2, self.j]
            #             continue

            for self.i in range(0, SIZE_X):
                for self.j in range(0, SIZE_Y):
                    if self.massiv_potential[self.i, self.j] == POTENTIAL_O_VAC or self.massive_for_check_vacancies[self.i, self.j] == 1:
                        continue
                    if self.i == SIZE_X - 1:
                        self.fil1 = 0
                    else:
                        self.fil1 = self.massiv_potential[self.i+1,self.j]
                    if self.i == 0:
                        self.fil2 = 0
                    else:
                        self.fil2 = self.massiv_potential[self.i-1, self.j]

                    if self.j == SIZE_Y - 1:
                        self.fil3 = 0
                    else:
                        self.fil3 = self.massiv_potential[self.i,self.j+1]
                    if self.j == 0:
                        self.fil4 = 0
                    else:
                        self.fil4 = self.massiv_potential[self.i, self.j-1]

                    self.massiv_potential[self.i, self.j] = (self.fil1 + self.fil2 + self.fil3 + self.fil4) / 4

            # for self.i in range(0,SIZE_X):
            #     self.massiv_potential[self.i, SIZE_Y-1] = 0
            #     if self.Zcol != 0:
            #         self.massiv_potential[self.i, self.Zcol] = POTENTIAL_O_VAC
            #     elif self.Zcol == 0 and self.i == 15:
            #         self.massiv_potential[self.i, self.Zcol] = POTENTIAL_O_VAC

            # for self.j in range(1,SIZE_Y-1):
            #     for self.i in range(0, SIZE_X):
            #         if self.i == 0:
            #             self.massiv_potential[0, self.j] = self.massiv_potential[1, self.j]
            #             continue
            #         if self.i == SIZE_X-1:
            #             self.massiv_potential[0, self.j] = self.massiv_potential[SIZE_X-2, self.j]
            #             continue

            for self.j in range(SIZE_Y-1,-1, -1):
                for self.i in range(SIZE_X-1, -1, -1):
                    if self.massiv_potential[self.i, self.j] == POTENTIAL_O_VAC or self.massive_for_check_vacancies[self.i, self.j] == 1:
                        continue
                    if self.i == SIZE_X - 1:
                        self.fil1 = 0
                    else:
                        self.fil1 = self.massiv_potential[self.i+1,self.j]
                    if self.i == 0:
                        self.fil2 = 0
                    else:
                        self.fil2 = self.massiv_potential[self.i-1, self.j]

                    if self.j == SIZE_Y - 1:
                        self.fil3 = 0
                    else:
                        self.fil3 = self.massiv_potential[self.i,self.j+1]
                    if self.j == 0:
                        self.fil4 = 0
                    else:
                        self.fil4 = self.massiv_potential[self.i, self.j-1]

                    self.massiv_potential[self.i, self.j] = (self.fil1 + self.fil2 + self.fil3 + self.fil4)/4

    def calc_wom(self, POTENTIAL_O_VAC):
        """
        Рассчет потенциалов для 2-х мерного случая

        :return:
        """
        """
        Заполняем массив около пластин
        """
        self.calc_wm(massiv_potential=np.zeros((SIZE_X, SIZE_Y)), massive_for_check_vacancies=np.zeros((SIZE_X, SIZE_Y)), POTENTIAL_O_VAC=POTENTIAL_O_VAC)

class DistributionElectricField():
    def __init__(self):
        pass

    def calc(self, massive_for_check_vacancies, POTENTIAL_O_VAC):
        self.massiv_field = np.zeros((SIZE_X, SIZE_Y))
        self.massive_for_check_vacancies = massive_for_check_vacancies

        for self.i in range(0, SIZE_X):
            for self.j in range(0, SIZE_Y):

                self.sum_Vo = 0
                for self._j in range(0, SIZE_Y):
                    if self.massive_for_check_vacancies[self.i, self._j] == 1:
                        self.sum_Vo += 1

                try:
                    self.E = (POTENTIAL_O_VAC) / ((SIZE_Y -self.sum_Vo)*MIDDLE_SPACE_TRAP)
                except:
                    self.E = (POTENTIAL_O_VAC) / (MIDDLE_SPACE_TRAP)
                self.massiv_field[self.i, self.j] = self.E

        # for self.i in range(0, SIZE_X):
        #     for self.j in range(0, SIZE_Y):
        #         self.massiv_field[self.i, self.j] = massiv_potential[self.i, self.j]/((SIZE_Y-self.j)*MIDDLE_SPACE_TRAP)

        # for self.i in range(0, SIZE_X):
        #     self.massiv_field[self.i, 0] = massiv_potential[self.i, 0] / (SIZE_Y*MIDDLE_SPACE_TRAP)
        #     self.massiv_field[self.i, SIZE_Y-1] = 0
        #
        # for self.i in range(0, SIZE_X):
        #     for self.j in range(0, SIZE_Y):
        #         if self.massive_for_check_vacancies[self.i, self.j] == 1:
        #             self.massiv_field[self.i, self.j] = massiv_potential[self.i, self.j]/((SIZE_Y-self.j)*MIDDLE_SPACE_TRAP)
        #             continue
        #
        #         self.E = 0
        #         for self.iE in range(0, SIZE_X):
        #             for self.jE in range(0, SIZE_Y):
        #                 if massive_for_check_vacancies[self.iE, self.jE] == 1:
        #                     self.dx = abs(self.i - self.iE)
        #                     self.dy = abs(self.j - self.jE)
        #                     self.E += massiv_potential[self.iE, self.jE] / ((math.sqrt(
        #                         ((self.dx**2) + (self.dy**2))
        #                     )*MIDDLE_SPACE_TRAP))
        #         self.massiv_field[self.i, self.j] = self.E


        return self.massiv_field

    def calc_wom(self, POTENTIAL_O_VAC):
        return self.calc(massive_for_check_vacancies=np.zeros((SIZE_X, SIZE_Y)), POTENTIAL_O_VAC=POTENTIAL_O_VAC)