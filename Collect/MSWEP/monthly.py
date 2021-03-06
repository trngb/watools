# -*- coding: utf-8 -*-
import sys
from watools.Collect.MSWEP.DataAccess import DownloadData


def main(Dir, Startdate, Enddate, latlim, lonlim, cores=False, Waitbar = 1):
    """
    This function downloads MSWEP precipitation monthly data for a given variable, time
    interval, and spatial extent.

    Keyword arguments:
    Dir -- 'C:/file/to/path/'
    Startdate -- 'yyyy-mm-dd'
    Enddate -- 'yyyy-mm-dd'
    latlim -- [ymin, ymax]
    lonlim -- [xmin, xmax]
    Waitbar -- 1 (Default) Will print a waitbar
    """
    if Waitbar == 1:
        print('\nDownloading monthly MSWEP precipitation data for the period %s till %s' %(Startdate, Enddate))

    # Download data
    DownloadData(Dir, Startdate, Enddate, latlim, lonlim, Waitbar, cores, TimeCase='monthly')

if __name__ == '__main__':
    main(sys.argv)
