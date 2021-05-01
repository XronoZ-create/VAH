import matplotlib.pyplot as plt

class DrawVAH():
    def __init__(self):
        self.current_points_1 = []
        self.potencial_points_1 = []
        self.current_points_2 = []
        self.potencial_points_2 = []


    def add_point_1(self, current, potencial):
        self.current_points_1.append(current)
        self.potencial_points_1.append(potencial)

    def add_point_2(self, current, potencial):
        self.current_points_2.append(current)
        self.potencial_points_2.append(potencial)

    def draw(self):
        with plt.rc_context({'axes.edgecolor': 'orange', 'xtick.color': 'red', 'ytick.color': 'green',
                             'figure.facecolor': 'white'}):
            # Temporary rc parameters in effect
            self.fig, self.ax = plt.subplots(1)
            self.ax.plot(self.potencial_points_1, self.current_points_1, 'b-o', markersize=3)
            self.ax.plot(self.potencial_points_2, self.current_points_2, 'r-o', markersize=3)
            self.ax.set_xlabel('U, напряжение')
            self.ax.set_ylabel('j, плотность тока Пула-Френкеля')
            self.ax.set_yscale('log')
            # self.ax.set_ylim([10**(-200), 0])

        plt.show()