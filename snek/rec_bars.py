# Author: Travis Cyronek
# Date: 30 August 2017
# Purpose: To add NBER recession bars to matplotlib graphs


import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader as pdr


def add_rec_bars(ax,begin=datetime.datetime(1854,12,1),end=datetime.datetime.today(),color='k',alpha=.2):

    """ 
    Description: This function adds recession bars to a matplotlib graph.
    To ensure it runs, the required packages are imported in this module.
    Note that the import names may differ from the user's, and so imports
    may need to be renamed (or changed here in the source code).

    Inputs:
    ax          -- the axis object that recession bars want to be added to
    begin / end -- datetime objects corresponding to the period of interest
    color       -- color of the recession bars
    alpha       -- desired fade of bars

    Outputs:
    ax  -- an axis with recession bars added 
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
