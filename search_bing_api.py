# import dependencies
from requests import exceptions
import argparse
import requests
import os

# import api key from credentials file
# for first time setup, create a credentials.txt file with the api key as a single line.
# link to get your own API_KEY: https://azure.microsoft.com/en-us/try/cognitive-services/my-apis/?apiSlug=search-api-v7
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
API_KEY = PRIVATE_API_KEY
MAX_RESULTS = 200
GROUP_SIZE = 50

# set the endpoint API URL
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

# when attempting to download images from the web with both Python and the requests library
# we can run into some errors so let's try to intercept them
EXCEPTIONS = {IOError, FileNotFoundError, exceptions.RequestException, exceptions.HTTPError, exceptions.ConnectionError,
              exceptions.Timeout}

# store the search term in a convenience variable then set the headers and search parameters
term = args["query"]
headers = {"Ocp-Apim-Subscription-Key": API_KEY}
params = {"q": term, "offset": 0, "count": GROUP_SIZE}

# make the search
print("[INFO] searching Bing API for '{}'".format(term))
search = requests.get(URL, headers=headers, params=params)
search.raise_for_status()

# grab the results from the search, including the total number of estimated results returned by the Bing API
results = search.json()
estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
print("[INFO] {} total results for '{}'".format(estNumResults,
                                                term))

# initialize the total number of images downloaded thus far
total = 0

# iterate over the estimated number of results in `GROUP_SIZE` groups
for offset in range(0, estNumResults, GROUP_SIZE):
    # update the search parameters using the current offset, then make the request to fetch the results
    print("[INFO] making request for group {}-{} of {}...".format(
        offset, offset + GROUP_SIZE, estNumResults))
    params["offset"] = offset
    search = requests.get(URL, headers=headers, params=params)
    search.raise_for_status()
    results = search.json()
    print("[INFO] saving images for group {}-{} of {}...".format(
        offset, offset + GROUP_SIZE, estNumResults))

# loop over the results
for v in results["value"]:
    # try to download the image
    try:
        # make a request to download the image
        print("[INFO] fetching: {}".format(v["contentUrl"]))
        r = requests.get(v["contentUrl"], timeout=30)

        # build the path to the output image
        ext = v["contentUrl"][v["contentUrl"].rfind("."):]
        p = os.path.sep.join([args["output"], "{}{}".format(
            str(total).zfill(8), ext)])

        # write the image to disk
        f = open(p, "wb")
        f.write(r.content)
        f.close()

    # catch any errors that would not unable us to download the
    # image
    except Exception as e:
        # check to see if our exception is in our list of
        # exceptions to check for
        if type(e) in EXCEPTIONS:
            print("[INFO] skipping: {}".format(v["contentUrl"]))
            continue