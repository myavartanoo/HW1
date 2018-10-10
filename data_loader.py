import zipfile
import numpy as np

def loader(file_name='hw1_data.zip'):
    archive = zipfile.ZipFile(file_name, 'r')
    almostsorted_10k = np.array(archive.read('10k_almostsorted.txt')[:-1].split(),dtype=int)
    random_10k = np.array(archive.read('10k_random.txt')[:-1].split(),dtype=int)
    almostsorted_50k = np.array(archive.read('50k_random.txt')[:-1].split(),dtype=int)
    random_50k = np.array(archive.read('50k_almostsorted.txt')[:-1].split(),dtype=int)

    return almostsorted_10k, random_10k, almostsorted_50k, random_50k

