# MY DATA SCIENCE JOURNEY STARTS FROM HERE

## Application of Machine Learning

1. Image analysis
2. Speech recognition
3. Disease prediction
4. Stock market analysis
5. Fraud detection
6. Recommedation systems

## Types of machine learning (5 types)

1. Supervised learning
   - It deals with labelled, structured dataset e.g image classification

### Algorithms of supervised learning

- Linear regression
- Logistic Regression
- Decision Trees
- Support vector Machines (SVM)
- k- Nearest Neighbor (KNN)
- Random Forest
- Deep Learning (CNN) - image classification, face recognition, video analysis

.h5 is file with the trained model

2. Unsupervised learning
   - it deals with unlabelled data, discovering hidden patterns, clusters, structures like market basket analysis, cancer analysis

### Algorithms of unsupervised learning

- K-means clustering
- Hierarchical clustering
- Principle Component Analysis

3. Semi supervised learning
   It deals with a mixture of labelled and unlabelled data

4. Reinforcement learning

- It deals with rewards of results of a performing machine

# MODEL TRAINING

1. You need module numpy, matplotlib, tensorflow
   os which is used for system interaction
   Tensorflow is used for building and training deep learning model
   Tensorflow has keras which used for high level API for neural networks
   Tensorflow image generator for augmentation(increase size or value of something by adding to it)
   Tensorflow sequential for linear stack of neural network layers
   Tensorflow layes where we have Conv2D, Maxpooling2D, Flattern, Dense, Dropout
   Tensorflow Adam for training
   Tensorflow for training callbacks
   Matplotlib for graphing

2. Seeding data for reproducibility
   for tensorflow and numpy which I recommend 42 for consistent results

3. Define the image size
4. batch size
5. Epochs 20 # number of full passes through the dataset
6. Number of classes
   - Number of output classes like crops(diseased, healthy)
7. Create a convolutional Neural Network model

# LINEAR REGRESSION
Supervised learning which helps finding correlation btn variables and this can help one to predict the continous output variable based on the one or more predictor.

it is used prediction forecasting, time series modeling

##  Types of Regressions
Linear regression
 1. Simple predict the dependent variable basing on an independent value
 2. Multiple used to estimate the relationship btn 2 or more independent variables and one dependent variable