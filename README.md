# keyboard_classification_cnn

Source dataset: http://www.vision.caltech.edu/Image_Datasets/Caltech101/

Uses Convolutional Neural Network for image recognition. In this case it is to classify different keyboard instruments. 

Currently the network uses 10 epochs for short training but sufficient for good image classification.

It algorithm follows the steps of the convolution: We select a feature detector (64x64 RGB) for convolving the image. We then reduce the size of feature maps for pooling, followed by flattening the layer into a string of nodes. Finally, we build a fully connected layer into a network akin to an artificial neural network.
