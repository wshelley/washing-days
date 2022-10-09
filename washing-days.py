#!/usr/bin/env python3
"""
Simple application to display days/times to hang washing out to dry at a given location lon/lat
"""

__author__ = "Wayne Shelley"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import requests
#import json
from logzero import logger


def main(args):
    """ Main entry point of the app """
    logger.info(args)
    print("hello world!!")
    print(args.lon)
    print(args.lat)
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=" + str(args.lat) + "&longitude=" + str(args.lon) + "&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m,direct_radiation&windspeed_unit=mph")
    print(response.status_code)
    print(response.json())

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