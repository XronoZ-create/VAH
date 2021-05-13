from modelling.const_variable import *
import math

s = C_AXIS

for _E in range(1, 100, 1):
    for _ebs in range(1, 1000, 1):
        ENERGY_IONIZATION_TRAP = (_E/10) * CHARGE_E
        E_INF = _ebs/10
        CONST_FRENKEL = np.sqrt((CHARGE_E ** 3) / (np.pi * E_INF * 8.85 * 10 ** (-12)))

        # s = 1.225*10**(-9)
        one_density_current_1 = (CHARGE_E / (s ** 2)) * (ENERGY_IONIZATION_TRAP / CONST_PLANKA) * \
                            math.exp(-
                                (
                                        ENERGY_IONIZATION_TRAP - (CONST_FRENKEL * math.sqrt(abs(16604859)) )
                                ) / (
                                        CONST_BOLTZMAN * 394
                                )
                            ) * math.tanh(
                                (
                                        (CHARGE_E * abs(16604859) * s) /
                                        (2 * CONST_BOLTZMAN * 394)
                                )
                            )

        # s = 1.225 * 10 ** (-12)
        one_density_current_2 = (CHARGE_E / (s ** 2)) * (ENERGY_IONIZATION_TRAP / CONST_PLANKA) * \
                                math.exp(-
                                         (
                                                 ENERGY_IONIZATION_TRAP - (CONST_FRENKEL * math.sqrt(abs(4815409309)))
                                         ) / (
                                                 CONST_BOLTZMAN * 598
                                         )
                                         ) * math.tanh(
            (
                    (CHARGE_E * abs(4815409309) * s) /
                    (2 * CONST_BOLTZMAN * 598)
            )
        )
        try:
            dif = math.log10(one_density_current_2) - math.log10(one_density_current_1)
            if dif < 6:
                print('W: {0}, ebs: {1}, dif: {2}'.format(_E/10, E_INF, dif))
        except:
            pass