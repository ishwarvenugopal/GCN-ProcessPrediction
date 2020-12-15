# Setting parameters for evaluation

```
path = PATH TO CSV FILE
dataset = CHOOSE FROM {'helpdesk','bpi'}
save_folder = PATH TO FOLDER WHERE THE MODEL WEIGHTS ARE STORED AFTER TRAINING
num_nodes = 9 (for 'helpdesk') OR 6 (for 'bpi') 
```

Different variants can be specified by choosing the following combination of parameters:

    | variant               | weighted_adjacency | binary_adjacency | laplacian_matrix |
    |-----------------------|--------------------|------------------|------------------|
    | 'weighted'            | True               | False            | False            |
    | 'binary'              | False              | True             | False            |
    | 'laplacianOnWeighted' | True               | False            | True             |
    | 'laplacianOnBinary'   | False              | True             | True             |

There are separate files for the MLP variant. 

```
num_runs = TOTAL NUMBER OF RUNS FOR EACH LEARNING RATE
```
If evaluation is only for a particular learning rate, then set the lr_optimum as follows:
```
lr_optimum = LEARNING RATE TO BE EVALUATED
```
If evaluation is for all learning rate used during training, then set the lr_optimum as follows:
```
lr_optimum = None
```


```python

```
