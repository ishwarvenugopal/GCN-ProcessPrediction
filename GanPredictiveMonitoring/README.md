The original implementation by Taymouri et al. can be found at [GanPredictiveMonitoring](https://github.com/farbodtaymouri/GanPredictiveMonitoring)

The following changes were made to the original code:

1 ) In ***main.py***:

```
if __name__ == "__main__"
```

 was inserted with all runs (k=2,4,6 for Helpdesk dataset and k=2,4,6,16,30 for BPI’12(W) dataset with each 25 epochs)


2 ) In ***preparation.py*** 

In 
```
def train_valid_test_index(cls)
```
, the split ratio was changed from 80:20 to 2/3 1/3 by changing the values for the parameters ‘a’ and ‘b’ as 
```
a =0.528 
```
and 
```
b= 0.062304 
```
and using the following lines of code:

```
train_inds = np.arange(0, round(cls.design_matrix_padded.size()[0] * a))
test_inds = list(set(range(cls.design_matrix_padded.size()[0])).difference(set(train_inds)))
validation_inds = test_inds[0:round(b* len(test_inds))]
test_inds = test_inds[round(b * len(test_inds)):]
```

The value of ‘a’ and ‘b’ was calculated as follows:

```
	Training set = 66% ; \\
	Validation set is 20% from Training set = 13.2%; \\
	Test set = 33% from full dataset

	Hence, we set the parameters to: 

	a = 0.66-0.132 = 0.528 ; 52.8% for train \\
	b = ( 1-0.528) * 13.2 = 0.062304 
```

