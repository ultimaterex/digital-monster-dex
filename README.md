# Digital Monster Dex

[![Keras](https://ultimaterex.gitlab.io/images.serubii/images/badges/made%20with-Keras-blue.svg)](https://keras.io/)


[![OpenCV](https://ultimaterex.gitlab.io/images.serubii/images/badges/made%20with-OpenCV-blue.svg)](https://opencv.org/)

The Digital Monster Dex uses Keras and OpenCV to distinguish different digital monster from eachother. training data was fetched using the bing search api.

# New Features!

  - Placeholder
  - Placeholder


### Tech

Digital Monster Dex uses a number of projects to work properly:

* [OpenCV](https://opencv.org/) -  is an open source computer vision and machine learning software library.
* [Keras](https://keras.io/) - Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.
* [Microsoft Cognitive Services](https://azure.microsoft.com/en-us/try/cognitive-services/?api=bing-image-search-api) - Cognitive Services let you build intelligent apps with powerful algorithms using just a few lines of code. 




### Installation

Digital Monster Dex requires [Python](https://www.python.org/) v3+ to run.

Install the required packages

```sh
$ pip install requests
$ pip install opencv-python
```

For workon environments...

```sh
$ workon your_env_name
$ pip install requests
$ pip install opencv-python
```

### How to use
1. For first time setup, create a credentials.txt file with the [API_KEY](https://azure.microsoft.com/en-us/try/cognitive-services/my-apis/?apiSlug=search-api-v7) on a single line.
2. Create a dataset folder and folders for the respective entities. 
    ```sh
    $ mkdir -p -- datasets/example datasets/example2 datasets/example3
    ```
3. For every entity in your data set, run search_bing_api.py to populate your datasets.
    ```sh
    $ python search_bing_api.py --query "example" --output dataset/example
    ```
4. To train the dataset
    ```sh
    python train.py --d dataset --m <name>.model --l lb.pickle
    ```


### Todos
 - Setup CNN
 - Validate Results
 - Setup REST API
 - Finish Readme
 

