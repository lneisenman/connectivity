# -*- coding: utf-8 -*-

from idtxl.multivariate_te import MultivariateTE
from idtxl.data import Data
from idtxl.visualise_graph import plot_network
import matplotlib.pyplot as plt

import mne_connectivity


def multivariate_TE(data):
    network_analysis = MultivariateTE()
    settings = {'cmi_estimator': 'JidtGaussianCMI',
                'max_lag_sources': 5,
                'min_lag_sources': 1}
    results = network_analysis.analyse_network(settings=settings, data=data)
    return results
