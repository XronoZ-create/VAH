import numpy as np
import matplotlib.pyplot as plt
import io
import glob
from PIL import Image

list_images = []
massive_field = np.zeros((30, 30))
fig, axs = plt.subplots(1, 3, figsize=(15,15))


# cb2.remove()
axs[1].set_title('Распределение напряженности')
axs[1].grid(True)

im2 = axs[1].imshow(massive_field.T, origin='lower', vmin=2, vmax=3, cmap='jet')
cb2 = fig.colorbar(im2, ax=axs[1], orientation='horizontal')

buf = io.BytesIO()
plt.savefig(buf, format='png')
list_images.append(buf)

plt.close('all')

fig, axs = plt.subplots(1, 3, figsize=(15,15))
axs[1].set_title('Распределение напряженности')
axs[1].grid(True)

im2 = axs[1].imshow(massive_field.T, origin='lower', vmin=-3, vmax=-2, cmap='jet')
cb2 = fig.colorbar(im2, ax=axs[1], orientation='horizontal')

buf = io.BytesIO()
plt.savefig(buf, format='png')
list_images.append(buf)

print(list_images)

img, *imgs = [Image.open(f) for f in list_images]
img.save(fp='my_gif.gif', format='GIF', append_images=imgs, save_all=True, duration=200, loop=0)

# plt.show()