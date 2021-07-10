# -*- coding: utf-8 -*-
"""
 Created on 2021/7/10 14:45
 Filename   : ex_plot_digits_agglomeration.py
 Author     : Taosy.W
 Zhihu      : https://www.zhihu.com/people/1105936347
 Github     : https://github.com/AFei19911012/PythonSamples
 Description:
"""

# =======================================================
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets, cluster
from sklearn.feature_extraction.image import grid_to_graph


def plot_digits_agglomeration():
    digits = datasets.load_digits()
    images = digits.images
    X = np.reshape(images, (len(images), -1))
    connectivity = grid_to_graph(*images[0].shape)

    agglo = cluster.FeatureAgglomeration(connectivity=connectivity,
                                         n_clusters=32)

    agglo.fit(X)
    X_reduced = agglo.transform(X)

    X_restored = agglo.inverse_transform(X_reduced)
    images_restored = np.reshape(X_restored, images.shape)
    plt.figure(1, figsize=(4, 3.5))
    plt.clf()
    plt.subplots_adjust(left=.01, right=.99, bottom=.01, top=.91)
    for i in range(4):
        plt.subplot(3, 4, i + 1)
        plt.imshow(images[i], cmap=plt.cm.gray, vmax=16, interpolation='nearest')
        plt.xticks(())
        plt.yticks(())
        if i == 1:
            plt.title('Original data')
        plt.subplot(3, 4, 4 + i + 1)
        plt.imshow(images_restored[i], cmap=plt.cm.gray, vmax=16,
                   interpolation='nearest')
        if i == 1:
            plt.title('Agglomerated data')
        plt.xticks(())
        plt.yticks(())

    plt.subplot(3, 4, 10)
    plt.imshow(np.reshape(agglo.labels_, images[0].shape),
               interpolation='nearest', cmap=plt.cm.nipy_spectral)
    plt.xticks(())
    plt.yticks(())
    plt.title('Labels')
    plt.show()


if __name__ == '__main__':
    plot_digits_agglomeration()
