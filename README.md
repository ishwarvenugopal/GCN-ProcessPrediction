## A Comparison of Deep-Learning Methods for Analysing and Predicting Business Processes

This repository contains the source code and the associated files for the paper titled 'A Comparison of Deep-Learning Methods for Analysing and Predicting Business Processes'

In this work, five different model variants were developed for the task of predicting the nature and timestamp of the next activity in a business process. This included four different variants of a model having a Graph Convolutional Network (GCN) layer and a Multi-layer Perceptron (MLP) model.

### Training 

The datasets used for training the model can be found in the *Data* folder.

Different GCN variants can be trained using *GCN_EventPredictor_(Training).ipynb* and *GCN_TimePredictor_(Training).ipynb*, by changing the parameter cell of the corresponding *.ipynb* file. 

* Choose one among the two datasets by commenting out the lines corresponding to the other dataset

* Different variants can be trained by choosing the following combination of parameters:

    | variant               | weighted_adjacency | binary_adjacency | laplacian_matrix |
    |-----------------------|--------------------|------------------|------------------|
    | 'weighted'            | True               | False            | False            |
    | 'binary'              | False              | True             | False            |
    | 'laplacianOnWeighted' | True               | False            | True             |
    | 'laplacianOnBinary'   | False              | True             | True             |

* For training MLP variants, use the *MLP_EventPredictor_(Training).ipynb* and *MLP_TimePredictor_(Training).ipynb* files.
* For each model variant, the training script will train 5 different runs each for three different initial learning rates for the optimizer.

Note: Separate python files for each variant and dataset, with the optimal learning rates for that particular variant can be found in the 'python_files' folder. Alternatively, these .py files can be directly run to train the model variants. 

### Evaluation

After training, the models can be evaluated at different quartiles based on the number of events and the case duration. The evaluation scripts are thus sorted into two folders accordingly.

*<Event/Time>Quartiles_<Event/Time>Predictor_(<GCN/MLP>).ipynb* contains the code to load the trained models and evaluate it at different quartiles sorted according to number of events or time (case duration). There are separate files for Event Predictor and Time Predictor, as well as for GCN and MLP variants. 


