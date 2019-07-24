# keyboard_classification_cnn

Source dataset: http://www.vision.caltech.edu/Image_Datasets/Caltech101/

Uses Convolutional Neural Network for image recognition. In this case it is to classify different keyboard instruments. 

Currently the network uses 10 epochs for short training but sufficient for good image classification.

It algorithm follows the steps of the convolution: We build feature detectors (64x64 RGB) for convolving the image. We then apply max pooling with a 2x2 pool to reduce the size of the features from the convolution step, resulting in a pool feature map.

Next, we apply the flattening operation to convert the map into a 1-dimensional vector of nodes for building the artificial neural network, which is then achieved with the Dense() method. 

Finally, the network is compiled and applied to train on different keyboard images
