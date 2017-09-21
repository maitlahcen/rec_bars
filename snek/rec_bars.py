# Author: Travis Cyronek
# Date: 30 August 2017
# Purpose: Add NBER recession bars to matplotlib graphs


import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as pdr


def add_rec_bars(ax,begin=datetime.datetime(1854,12,1),end=datetime.datetime.today(),color='k',alpha=.2):

    """
    Description: This function adds recession bars to a matplotlib graph. The
    function is intended to be used with Pandas DataFrames / Series where the
    indexes are datetime objects (this ensures that the recession bars are
    added along the appropriate axis on the correct dimension).

    Inputs:
    ax          -- (axis object) the axis that recession bars want to be added to
    begin / end -- (datetime objects) dates corresponding to the period of interest
    color       -- (string) color of the recession bars
    alpha       -- (float) desired fade of bars

    Outputs:
    ax  -- (axis object) an axis with recession bars added
    """

    bot, top = ax.get_ylim()
    rec_bars = pdr.DataReader('USREC','fred',begin,end)
    rec_bars = np.multiply(rec_bars,top)
    for i in range(len(rec_bars.index)):
        if rec_bars['USREC'][i] == 0:
            rec_bars['USREC'][i] += bot

    ax.set_ylim([bot,top])
    ax.fill_between(rec_bars.index,
                    np.ravel(rec_bars.as_matrix()),
                    np.zeros((len(rec_bars),))+bot,
                    linewidth=0,color=color,alpha=alpha)

    return ax
