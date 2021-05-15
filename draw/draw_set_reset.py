# Рисование кислородных вакансий по существующим координатам.
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from modelling.const_variable import *
import matplotlib.ticker as ticker
from contextlib import suppress
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
from matplotlib.colors import LogNorm
import io
from PIL import Image
from celluloid import Camera

class DrawSetReset():
    def __init__(self, num_plots):
        matplotlib.use("TkAgg")
        self.num_plots = num_plots
        self.fig, self.axs = plt.subplots(1, num_plots, figsize=(15,15))

        self.norm = mpl.colors.Normalize(vmin=5, vmax=10)

        self.list_images = []
        self.camera = Camera(self.fig)

    def draw_vacancies(self, coordinate, legend=None):
        self.axs[0].xaxis.set_major_locator(ticker.MultipleLocator(1))
        self.axs[0].yaxis.set_major_locator(ticker.MultipleLocator(1))
        self.axs[0].set_xlim(0, SIZE_X)
        self.axs[0].set_ylim(0, SIZE_Y)
        self.axs[0].grid(True)
        self.axs[0].set_title('Кислородные вакансии')

        self.list_coordinates = []
        self.x_coordinates = []
        self.y_coordinates = []
        for self.one_coord in coordinate:
            self.list_coordinates.append(self.one_coord)

        for self.coord in self.list_coordinates:
            self.x_coordinates.append(self.coord[0] + 0.5)
        for self.coord in self.list_coordinates:
            self.y_coordinates.append(self.coord[1] + 0.5)
        self.axs[0].scatter(self.x_coordinates, self.y_coordinates, s=(25/(SIZE_Y*SIZE_X))*1000)
        if legend != None:
            self.axs[0].annotate('U=%s'%legend, xy=(SIZE_X, SIZE_Y), size=14, ha='right', va='top', bbox=dict(boxstyle='round', fc='w'))
        # self.camera.snap()

    def draw_electric_field_distribution(self, massive_field):
        with suppress(Exception):
            self.cb2.remove()
        self.axs[2].set_title('Распределение напряженности')
        self.axs[2].grid(True)

        if massive_field[0, START_POTENTIAL_DOT_J] > 0:
            self.im2 = self.axs[2].imshow(massive_field.T, origin='lower', vmin=FIELD_VMIN, vmax=FIELD_VMAX, cmap='jet')
        elif massive_field[0, START_POTENTIAL_DOT_J] < 0:
            self.im2 = self.axs[2].imshow(massive_field.T, origin='lower', vmin=-FIELD_VMAX, vmax=-FIELD_VMIN, cmap='jet')
        self.cb2 = self.fig.colorbar(self.im2, ax=self.axs[2], orientation='horizontal')

    def draw_temp_distribution(self, massive_temp):
        with suppress(Exception):
            self.cb3.remove()
        self.axs[3].set_title('Распределение температуры')
        self.axs[3].grid(True)

        self.im3 = self.axs[3].imshow(massive_temp.T, origin='lower', vmin=0, vmax=600, cmap='jet')
        self.cb3 = self.fig.colorbar(self.im3, ax=self.axs[3], orientation='horizontal')

    def draw_potential_distribution(self, potential):
        with suppress(Exception):
            self.cb1.remove()
        self.axs[1].set_title('Распределение потенциала')
        self.axs[1].grid(True)
        if potential[0, START_POTENTIAL_DOT_J] > 0:
            self.im1 = self.axs[1].imshow(potential.T, origin='lower', vmin=POTENTIAL_VMIN, vmax=POTENTIAL_VMAX, cmap='jet')
        elif potential[0, START_POTENTIAL_DOT_J] < 0:
            self.im1 = self.axs[1].imshow(potential.T, origin='lower', vmin=-POTENTIAL_VMAX, vmax=-POTENTIAL_VMIN, cmap='jet')
        self.cb1 = self.fig.colorbar(self.im1, ax=self.axs[1], orientation='horizontal')

    def create_animation(self):
        # self.anim = self.camera.animate()
        # self.anim.save('scatter.gif')
        self.img, *self.imgs = [Image.open(self.f) for self.f in self.list_images]
        self.img.save(fp='scatter.gif', format='GIF', append_images=self.imgs, save_all=True, duration=200, loop=0)

    def snap(self):
        self.buf = io.BytesIO()
        plt.savefig(self.buf, format='png')
        self.list_images.append(self.buf)
        # self.camera.snap()

    def clear_plt(self):
        plt.clf()
        self.fig, self.axs = plt.subplots(1, self.num_plots, figsize=(15, 15))
        self.norm = mpl.colors.Normalize(vmin=5, vmax=10)