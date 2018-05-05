import glob
# import pyssim
# import math, operator
import hashlib
from PIL import Image
import os
from contextlib import suppress
from tqdm import tqdm

__author__ = 'perevera'


PATH = "/home/perevera/Imágenes/Piña Buena 2007, Salamanca - Oporto"
pics = sorted(glob.glob(os.path.join(PATH, "*.jpg")))
num = len(pics)
reps = []
print("Number of files: {}".format(num))

prev_img = Image.open(pics[0])
prev_hash = hashlib.md5(prev_img.tobytes()).hexdigest()

# Comprueba imágenes consecutivas idénticas

print("Looking for consecutive duplicated images...")

# for i in range(1, num-1):
for i in tqdm(range(1, num-1)):
    this_img = Image.open(pics[i])
    this_hash = hashlib.md5(this_img.tobytes()).hexdigest()
    if prev_hash == this_hash:
        # print("Duplicated images: {} - {}. Hash: {}".format(pics[i-1], pics[i], this_hash))
        reps.append(pics[i])
    prev_hash = this_hash

print("Number of consecutive repeated images: {} of {}".format(len(reps), num))

# Borra los ficheros repetidos y los elimina de la lista original

print("Removing consecutive duplicated images...")

for r in tqdm(reps):
    with suppress(OSError):
        # print("Removing duplicated image: {}".format(r))
        os.remove(r)
        pics.remove(r)
