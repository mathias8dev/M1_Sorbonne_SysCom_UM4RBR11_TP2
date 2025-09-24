# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 13:55:33 2025

@author: cathe
"""

import numpy as np
from matplotlib import pyplot as plt

def plotGallery(images, n=16, title=None):
    # Affiche les n premières images contenues dans images
    # images est de taille Nb image*Ny*Nx
    n = min(n, images.shape[0])
    nSubplots = int(np.ceil(np.sqrt(n)))
    fig, axs = plt.subplots(nSubplots, nSubplots)
    for i in range(n):
        axs[i // nSubplots, i % nSubplots].imshow(images[i], cmap=plt.cm.gray)
        axs[i // nSubplots, i % nSubplots].set_xticks([])
        axs[i // nSubplots, i % nSubplots].set_yticks([])
    if title:
        plt.suptitle(title)
    plt.show()

   
    
# #############################################################################
# I Chargement des données

# I.a. Chargement de la base
[X, y, name]=np.load("TP1.npy",allow_pickle=True)
plotGallery(X)

plotHistoClasses(y)