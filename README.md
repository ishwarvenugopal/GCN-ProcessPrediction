## Quartile-Based Prediction of Event Types and Event Time in Business Processes using Deep Learning 

This repository contains the source code and the associated files for the MSc Thesis titled 'Quartile-Based Prediction of Event Types and Event Time in Business Processes using Deep Learning'

In this work, five different model variants were developed for the task of predicting the nature and timestamp of the next activity in a business process. This included four different variants of a model having a Graph Convolutional Network (GCN) layer and a linear Multi-layer Perceptron (MLP) model.

### Training 

Different GCN variants can be trained using *GCN_EventPredictor_(Training).ipynb* and *GCN_TimePredictor_(Training).ipynb*, by changing the parameter cell of the corresponding *.ipynb* file. 

* Choose one among the three datasets by commenting out the lines corresponding to the other two datasets
* Change the *lr_value* parameter for different initial learning rates in the Adam optimizer
* Keep the *seed_value* as 42 for the same results as reported in the thesis

Different variants can be trained by choosing the following combination of parameters:

| variant               | weighted_adjacency | binary_adjacency | laplacian_matrix |
|-----------------------|--------------------|------------------|------------------|
| 'weighted'            | True               | False            | False            |
| 'binary'              | False              | True             | False            |
| 'laplacianOnWeighted' | True               | False            | True             |
| 'laplacianOnBinary'   | False              | True             | True             |

For training MLP variants, use the *MLP_EventPredictor_(Training).ipynb* and *MLP_TimePredictor_(Training).ipynb* files.
