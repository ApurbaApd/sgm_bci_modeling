import numpy as np
import math


def mag2db(y):
    """Convert magnitude response to decibels for a simple array.

    Args:
        y (numpy array): Power spectrum, raw magnitude response.

    Returns:
        dby (numpy array): Power spectrum in dB

    """
    dby = 20 * np.log10(y)
    return dby

def ccc(x,y):
    """ Concordance Correlation Coefficient """

    sxy = np.sum((x - np.mean(x))*(y - np.mean(y)))/x.shape[0]

    return 2*sxy / (np.var(x) + np.var(y) + (np.mean(x) - np.mean(y))**2)