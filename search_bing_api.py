# import dependencies
from requests import exceptions
import argparse
import requests
import os

# construct the argument parser and set it up
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True,
                help="search query to search Bing Image API for")
ap.add_argument("-o", "--output", required=True,
                help="path to output directory of images")
args = vars(ap.parse_args())

# set your Microsoft Cognitive Services API key along with the
# maximum number of results for a given search and  the group size
# for results (maximum of 50 per request)
API_KEY = "YOUR_API_KEY_GOES_HERE"
MAX_RESULTS = 250
GROUP_SIZE = 50

# set the endpoint API URL
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"