#!/usr/bin/env python3
"""
Simple application to display days/times to hang washing out to dry at a given location lon/lat
"""

__author__ = "Wayne Shelley"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import requests
import json
import pandas as pd
import numpy as np
import datetime
from logzero import logger

def main(args):
    """ Main entry point of the app """
    logger.info(args)
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(args.lat) + "&longitude=" + str(args.lon) + "&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m,direct_radiation&windspeed_unit=mph")
    data = response.json()['hourly']
    df = pd.DataFrame(data)
    df['ideal_conditions'] = np.where((df['temperature_2m'] > 0) & (df['relativehumidity_2m'] < 90) & (df['precipitation'] == 0) & (df['windspeed_10m'] > 3) & (df['direct_radiation'] > 10), True, False)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print("Ideal Times for Drying Outside")
    print(df.query('ideal_conditions == True'))
    print()
    print("Summary of Ideal Times for Drying Outside")

    df = df.reset_index()  # make sure indexes pair with number of rows
    first_time = None # reset search for ideal conditions
    for index, row in df.iterrows():
      if (row['ideal_conditions'] == True):
        if first_time == None:
          first_time = datetime.datetime.fromisoformat(row['time'])
      if (row['ideal_conditions'] == False):
        if first_time != None:
          time_difference = datetime.datetime.fromisoformat(row['time']) - first_time
          if (time_difference > datetime.timedelta(hours=4)):
            finish_time = datetime.datetime.fromisoformat(row['time'])
            print(str(first_time) + " for " + str(time_difference.seconds//3600) + " hours. Finishes at " + str(finish_time))
          first_time = None # reset search for ideal conditions

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Location argument
    parser.add_argument("--lon", required=True, type=float, action="store", dest="lon", help="Longitude Location String (e.g '55.75' is for West Linton)")
    parser.add_argument("--lat", required=True, type=float, action="store", dest="lat", help="Latitude Location String (e.g '3.35' is for West Linton)")


    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)