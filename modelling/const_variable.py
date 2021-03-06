import numpy as np

EFECTIVE_FREQ_VIBRATION = 1 * (10 ** 13)  # Эффективная частота вибрации. (f)
DIELECTRIC_CONST = 8.5  # Диэлектрическая проницаемость ZnO (e)
COEF_COMMUNICATION_POLAR = 40  # Коэффициент поляризации связи (b)
CONST_BOLTZMAN = 1.38 * (10 ** (-23))  # Постоянная Больцмана (kB)
CHARGE_E = 1.6 * (10 ** (-19))  # Заряд электрона (qE)
# POTENTIAL_O_VAC = 0.1  # Потенциал кислородной вакансии (QE)
TEMP_O_VAC = 600  # Температура кислородной вакансии (QT)
dt = 0.1  #
# THERMAL_CONDUCTIVITY = 1  # Теплопроводность (a)
h = 1  #

TIME_FORMATION_O_VAC = 1 * 10**(-11)  # время формирования вакансии
HEIGHT_MIGRATION_BARRIER = 2.5 * 1.6 * (10 ** -19)  #
FORMING_COEF_ENHANCEMENT = 32 * 10**(-28)  #

# Константы для рекомбинации
RECOMBINATION_ENHANCEMENT_FACTOR = 1 * 10**(18)  #
LATTICE_CONST = 623 * 10**(-12)
DRIFT_COEF = 3.55 * 10**(-10)  #
CONCENTRATION_DECAYING_LENGHT_IONS = 0.5 * 10**(-44)  #
U_CONST = 1

SIZE_X = 5  # 30
SIZE_Y = 10  # 50
THICKNESS_CONTACT = 2
WIDTH_CONTACT = 5

M_COEF = 30/SIZE_Y

POROG_GEN = 0.9
POROG_REC = 0.9

# Константы для рассчет тока Пула-Френкеля
ENERGY_IONIZATION_TRAP = 1.4 * CHARGE_E  # энергия ионизации ловушки
E_INF = 4.2
CONST_PLANKA = 6.62 * 10 ** (-34)  # постоянная Планка
CONST_FRENKEL = np.sqrt((CHARGE_E**3)/(np.pi*E_INF*8.85*10**(-12))) # постоянная Френкеля
CURRENT_OGR = 1 * 10**(500)
C_AXIS = 623 * 10**(-12)
MIDDLE_SPACE_TRAP = C_AXIS # среднее расстояние между ловушками 623 * 10**-12
ZERRO_CURRENT = 1 * 10**(-10)

# Константы для пропорционального рассчет тока Пула-Френкеля
A_CONST = 1*10**(-1)
B_CONST = 35

# Константы для рассчета омического тока
ELECTRICAL_CONDUCTIVITY = 1
ELECTRON_MOBILITY = 1
EFFECTIVE_DENSITY_STATES = 1  # Nc
CONDUCTION_BAND = 1  # Ec
FERMI_ENERGY = 1  # Ef

# Константы для пропорционального рассчета омического тока
A_CONST_OHMIC = 1
B_CONST_OHMIC = 1

# Константы для рассчета температуры
EQUAL_THERMAL_RESISTANCE = 5 * 10**5

TEMP_ENVIRONMENT = 323
NUM_RAND_V0 = 5  # 20

START_U_FORM = 0
MAX_U_FORM = 2000
STEP_U_FORM = 500
SMALL_STEP_FOR_ZERO = int(STEP_U_FORM/2)


POTENTIAL_VMAX = MAX_U_FORM / 1000
POTENTIAL_VMIN = 0
FIELD_VMAX = POTENTIAL_VMAX/MIDDLE_SPACE_TRAP
FIELD_VMIN = (POTENTIAL_VMIN/SIZE_Y*MIDDLE_SPACE_TRAP) - 0.1*(POTENTIAL_VMIN/SIZE_Y*MIDDLE_SPACE_TRAP)

STEP_FRIX_TEMP = 10

START_POTENTIAL_DOT_J = 3  # точка начального распределения напряженности
SAVE_PLOT_SET_RESET = True