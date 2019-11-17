# Digital Monster Dex

[![Keras](https://img.shields.io/badge/made%20with-Keras-blue.svg?style=for-the-badge&logo=data:image/png+xml;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAA6lBMVEXQAAD%2F%2F%2F%2FPAQPSAAL99PX00M778fPMAADwyMv9%2F%2F%2F%2B%2FP%2F6%2F%2F%2FUAAD%2F%2FfvrtbT78fHYTU3IAAD98ev4%2F%2F%2F8%2Fvn%2F%2B%2FX6%2Ff%2F%2F%2FPvhgobcZmn87O3%2B%2Fvj5%2F%2FvNAAbgb3DbcWrshYrbaGXCAADkko7giozfd3XbenPsxMLSGh%2FxwsPvtLfrfoH9%2F%2B%2Fln53RKyz24tnw1NL1zsPs0dTKCxLzsK7nuK%2FsvK3usbbrwcnql5r44uPUPj%2FYMC3aJSntfIDyub3ZWVr12NDbaFHYR0Xpr6XshoDfiH7tsaThm5vqnY%2FSZmHplYDYYVnTKSAzPxNoAAABBklEQVR42u3VsU7DMBAG4DvXWPXQ2API4KWqisCLASliCUisHer3fx24nhRXDOmdmJD6L06ifD6fLSVggzIJAuhinJqswpX8lRgDvx9cIJ%2B11gY9rf4kLpLsEac%2Bb6R7fF4kCRHdTEpG1JHYhZCU7FlISa8hJb2GlPQaQjLX%2BAIxiSwGEJPShYxY6oOFmHCNzVZK5ng76oimF84bUg4KMphMgytiMgAcLbWzlpJ3uqonvBefPmUikj405OGWzFpD4NFTO4OGQOalaUi0ZKZRQeDAW64h5vVkdgoCxzte2gXimXDu%2BQuwRG7OXugH%2BrRE4KUVOM%2FYWivXf%2BW%2FIA5WqpgAyQVd0jeEyR9QPydkNQAAAABJRU5ErkJggg%3D%3D)](https://keras.io/)


[![OpenCV](https://img.shields.io/badge/made%20with-OpenCV-blue.svg?style=for-the-badge&logo=data:image/png+xml;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAvCAYAAAChd5n0AAALU0lEQVR4AaVZa4yU1Rl%2BZrBtTJo0Kb%2BapmlqGn%2B0adGEphpMin8aLbAVja0tEKtWKMguXgC1gFwEAUEN3hUETFW0AgaiWFkMqIi6l93Z2bnszM73zezuzOyyu%2FPNzC5zmd395vS8J3PCTM6ZnYH98WTme%2Bdc3ue87%2FOec74BY0wgmUzCMAyYplmXjVBuC4VC6DUNTGUuYcLvRfbV15HZ%2BjQyG%2F%2BN4s5nYO%2FajeyLLyH%2B5VkM%2BHtRLBZrjUe2un0hAw0qjTTAdE4r7Wze17ISiAQDGD7yDiYbFjHb4WBFB5gNsCJ9x%2BVn%2Bi1%2F660s%2F8nHmMpm%2BXgWQkaIj6clUrd%2F4oGQSqUktDZCNVvC40H23mWYkk4D08KGgxMCK%2FzjXqR59JIpPp9%2Bjrr9kyzpB8lUsiy3UUgVm8Ft8fPnkZ03j03NctYgoEf%2BD%2FNZwe%2BnyOrmqNs%2FbUM5oGVZSmeyFVlRhLuv243sn25ntj4S9ZO57TY2MTpC4yvz1uufkm%2FhcHhaG4XRNEz0m2Hk1q2FIACVCKVOkSD0UZ2k%2FD2zYgXY1CSKYg5V7NP5R9Aaa1UKeo59fBKTTmel82UkJmddw8Y3PQnr6Aewm09jcvduTM36XlVSUxy5r89Tik1btarZ6IFCRJ8S5aJTfhMYHUVu%2BXLo0mmSO5pubIRlhJBIpir6jff1IUflWEPGpqg88ADGLDm%2F9Ku2f4SrEnsuEkb%2BmlkaXXASnKDp82nHSyUt2Pk88uvWcTJOpf%2BEcxbrP38BqZmIndhNS8QoEbGSKHxxTutI%2FtprWbS1ZZqJU0IDE4NxFGbP1haI0XffpTlk37r9u%2BKd3eK20W1bOBEojow%2FysVvT9Ucrz%2FSh%2ByWzdBFNPvcXlhXu7NfERHK102boBPsxe07YNczca%2BBS4cPaTWWeeYZJC3ryonkcjmCCF08HidIGzUUz4ODg5fbJVNIbd4CW0MkyStTNpfjyE47XpynVurAAW1Exrdu40QSiMVi1LYu%2Fwi6fKtqC5U0kt23D7ZTXc3cho2IGKGa4qTNdGztY1oiIxs3IJlS%2Bs5I7GTTV62zZ2E71D2k8OPZLNbWKvuqE5dsUyT2n%2FxUu58MHz6kEKnHP10aaUOXz%2BchbYNt7cjzDa9yRR0C4489ioxlaccjEQ9Ho7i0aQNsbfl1skwgQESU1Krln1Y45cLW7ab9vSFkli2RjiiRye%2FchYRpwKS%2B5uW%2BqVgUY5yEOCU7KvvRc%2B6fD3A2E%2FqdvYZ%2FyGazAlJMQ0ND0kadFZtsZ%2F3vU0w69Cfe%2FC%2BvZ3S0H6QVLOs7Fg4jN3euQoJA5Maam3m7TPlK1%2BUfgXJfl9NkVzRCEAIrMtiFAjKNTcpxw%2BYYee01akeiLstpU1S8zPHjsDXHk9z69RRpRcR1%2Bnd1R5Ri6WY42OFCds5vylKMO3TzTazf56k63tT4GAq3i6M%2FB0Sf%2FJwb2FQ8NoP7iCr2ugUW48jz57zXgwJ3hBwjAY%2Bf%2FkwJe7nYY7E4EsePYap0ci5cdx0bPneOt4uVzVFV7NVste7stV8%2B0CXrUjCAzF2L2fiypaxYyNccLxIIILviQRT%2BcjezutxyvKu%2Bsys7O608iUmWWmkjVLNlhU2UVQx5unk0ao8X58jQxYw%2F15ijbv%2F0V8mQKU67w9YQXBe%2Fwaf9R7DTtRLr2ufjic4%2F4s2ezTgbO4kvek4jLAsAE8Ke0TuAmWiEOpd2TjLaQsgBw48j3jewpu13bHXbHNbYdiNraruBNXLQp%2FxOeLxtES5Em3n4bemMshOrd%2ByiWCiyJ6wEPauVkTHNeEUBw1Dv7BWhi8UH0Rn9Fk%2B2L4RwVJC4YVqsavstOxF4m9JFe8iTKVNpiyM6mMLqbR58%2BkWkJNiKdlUPje%2BcNPGde5jbskimdDu7lcTn%2FpNoaptLDtaNra6%2FITbSD%2BMKjt2u7j40NHrgWOhmC1d1wes363jTmEKrqw8%2Fauhi3%2Bc41zKsij3P4R3sxJqW37PG9jlXROTb%2BGmkRTRj8kymPaflc3mk0mkY4QHc1UQkuhnBucjDDh8NUESon2ibTqeVM17CsrB2txdY5Bb9frjIxS50xCqP8aSJrZ1%2FR2N7dYdJKw%2FxNCKiBGq7y7UCQaOnbnFaSQuvvtcHLPQwBwdKRG65r5uNpvP6I3tIjIfzbf34waIuRlGUZBr4goxlJ4S2heiOew9idTUCHBs7%2F4w3unbghO8IPjGO4GBgBx5pu5ldCH4OQy9OhQjN0%2BLu4864OAG3IEEgQkTm9SP9CIf7FLHT%2BIGQiaWPd5eiKOEW%2BOBUFKxYBJLjI9jYeQf0kbiRHe5%2BDr0DQeTF%2FkCHN4unURS%2BcDey%2BYxuJ1bETs%2B022992Q8ZiXIijgVutvRxL6x0ltpVjEfPLd1DcC7oovYK5t3nYiEzDgStTi7wGxUCTTx1%2FuN5ASGzVwp2Rn8DJMcn8LM7O5lChKfJ4iY3fH6zynhF2EUbb7wfgXMR70Mo6z%2BLP39y1gQ%2BMvYraUUa2MCjRNWoXHQEy7KkTYpTlkut2KkIkM0TTMC50K0SWeBiX7XyeWJR%2FXilCF8cHcNtq7rBiSsLsW1fF7DPvRZN7RSRyqgc6tqDVO1dV9mY1KtpUfQ9dDxYyvFKR%2B55IoCCLTa6muMd%2BG%2BYE6mMCD1vfCUI7PHdD2Xj42n1WeBDpGZ%2BpCg5GMLzB3zQ5fjTXDdFJojUHO%2B8K0mLoWhs%2BbO9wIuBhyCPIeWV6vzAKd37VsWWSFpIp9IYS45x4vw5YcGyRiB%2Bty63fetoUEtky74eWAm641s0nnYu%2Be63%2BZuLChFwIvfvCAH7fZuFRlaX7SFNHB%2BZB7R3drKVC3uSFbDHswKr2n7NVnL8q4V%2FtvxKfD%2FmPUDtxIp%2F9s0QeJlViCx%2B2A8jHK1dPCwLz%2B33cZ1VCp5Sde3eXuCEeQgUDRJ4OZFNrjsQHYnALP0nQc7I%2F0dkNaIrr5n2obFVRFPBhd4z1FekTW9fGs5STpevqpOL%2FfS5IB%2FvstM0R%2BV9hGFoZAzzH%2Bxmitg5drzUBXwZOI0Kocvo8ALwofEybDYpT6syfwUBIuY3PdjeSRqj9pURfbR1HtKFEcg8d%2FvC%2BPmdHTSxUnWWrO%2Bm8kykFY2EjBAnGcaeA72Y1eCh9krV6%2FBbQI%2Fpx4b2BdrjCRF8P%2FQSMpNpGLSfyDfqRRtDmT7scj2o30hb57B3e%2FfydlOSiHDmqX20ISoryp3zsmXrA2hxRXi7CCxLvLgQ8AfC2PkyT6kF1F7FLfd3s3SmANHpTORYqQTryTzcfhM76H4WH3uOodk8if38YkXnLn17IjKX%2BS52koArBOsJJXDNQpfijLOUbk6%2Bw6%2Fc4sOJU31oPjeC19%2BPYnaDm9KRUCFwuQgHj5pIpiyIFMnbGex2LUfN%2B0c7ofbp%2BER4P3c%2BIS9AsgwLQs8fDMLRoF9dh4Qgxgks8FRvx48si9e45RWAiNhiknAigMfabgU5MhPs7XoI2ckxSkHNn5cW%2FEEDS9e5Kd9l9bliUL%2Fr%2F%2Bph7Z6hy%2FcR8aW04XhGW7G2Y%2F5Vk9nWuQQdoW%2Bp4kz7km1wNIuG1R44r4IIReoXd3vYqc9Nugfp38ZTmkXG%2FHiq4x6hGX0B0B%2F13%2Bp5Gun8cPl4VU8AlAVdHgOPbPfCsUA6WIMAaYinZMMqL85%2BLSItIiznqNilrZI4h62LODNwFBs67qDSTOVYe9Ei7HGvxIWBMxhJDJIuaPBpTwIVz8k0mr8cwD1rvJB6kJcmEOQGysV90xIXe%2FO9HvRHh7VzTHPHtjGUiOOr4Dkcdr2Aw4G9eJvjLe9uvNa5Ax94XkUk7cdEMU8LUPMYX91mIRiK4OvvQnjvRJyXWgNPvdCL9TsC2P6sF6%2B83YdOfwIDcYv6Vb1S%2FB9FMUjlXVhVZQAAAABJRU5ErkJggg%3D%3D%0A)](https://opencv.org/)

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
 

