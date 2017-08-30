# Author: Travis Cyronek
# Date: 30 August 2017
# Purpose: To add NBER recession bars to matplotlib graphs


import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as pdr


def add_rec_bars(ax,begin,end):

    """ Description: This function adds recession bars to a matplotlib graph.
        To ensure it runs, the required packages are imported in this module.
        Note that the import names may differ from the user's, and so imports
        may need to be renamed (or changed here in the source code). """

    """ Inputs:
        ax          -- the axis object that recession bars want to be added to
        begin / end -- datetime objects corresponding to the period of interest """

    """ Outputs:
        ax  -- an axis with recession bars added
        plt -- pyplot command limiting the vertical scope of plot to input specs """


    bot, top = ax.get_ylim()
    rec_bars = pdr.DataReader('USREC','fred',begin,end)
    rec_bars = np.multiply(rec_bars,top)
    ax.fill_between(rec_bars.index,np.ravel(rec_bars.as_matrix()),np.zeros((len(rec_bars),))+bot,alpha=.2,color='k')
    plt.ylim([bot,top])

    return ax, plt
