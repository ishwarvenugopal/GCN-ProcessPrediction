Separate python scripts for each set of configurations (with the optimal parameters for that configuration) is available here


So basically there are scripts for 
- two types of tasks (Event-Predictor and Time-Predictor) 
- on two datasets ( helpdesk, bpi ) 
- for five model variants ( weighted, binary, laplacianOnWeighted, laplacianOnBinary, mlp ). 

So the name of each of the .py files follow this pattern:

(Task)\_(dataset)\_(variant).py


Each .py script will have 5 runs each coded in them. The model parameters and the accuracy/loss values get saved in the Results folder for each of the runs (i.e 2 files per run). 

