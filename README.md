Bike-rider Detector
==============================

This repository illustrates how to create a bike-rider detector using Tensorflow so that we can use the detector to count the number of bike-riders in the street.

<img src="report/bikedetector2.png" width="400">

## Overview

1. Collect images of bike-riders from Google and Pixabay.
2. Label them with [LabelImg](https://github.com/tzutalin/labelImg)
3. Transfer learning from existing network using Tensorflow
4. Result

In general, this repository's codes are largely adopted from the posting below:
https://towardsdatascience.com/how-to-train-your-own-object-detector-with-tensorflows-object-detector-api-bec72ecfe1d9


## Data Collection

I collected total 396 images with bike riders, 324 from Google image search and 72 from Pixabay. You can see the images in the data/training/image folder. Don't forget resize the scraped images before labeling. You can use resize_images.py under src folder. 

## Labeling

Then I annotated the region of bike riders in each image with [LabelImg](https://github.com/tzutalin/labelImg) tool, which makes to labeling process much convenient. I assigned 'bikerider' label on bike riders. You can find annotations for each image under data/training/annotation.

## Create dataset

1. Split train and test dataset
  - use split_train_test.py
  - this will create csv files that will be fed into next step
2. Convert the two dataset into tfrecord format
  - separately apply generate_tfrecord.py to train and test dataset
  

## Transfer learning

We are going to use Tensorflow Object Detection API to train a detector. See [here](https://github.com/tensorflow/models/tree/master/research/object_detection) to set up it.



## Result
<img src="report/bikedetector1.png" width="400">
<img src="report/bikedetector3.png" width="400">

