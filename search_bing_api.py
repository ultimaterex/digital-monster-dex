# import dependencies
from requests import exceptions
import argparse
import requests
import os

# import api key from credentials file
# for first time setup, create a credentials.txt file with the api key as a single line.
with open('credentials.txt', 'r') as file:
    PRIVATE_API_KEY = file.read().replace('\n', '')


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
API_KEY = PRIVATE_API_KEY
MAX_RESULTS = 200
GROUP_SIZE = 50

# set the endpoint API URL
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"