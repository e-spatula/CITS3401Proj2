The report can be found in html format as ```report.html```. Should you wish to execute any of the code on your computer 
the notebook used to produce the report is ```report.ipynb```. Please note many of the examples run four jobs simulataneously 
on four CPU cores, if you do not have four cores you may need to change these cells. A find and replace on ```n_jobs=4``` should suffice.

There are three libraries that were written to keep the notebook clean:

1. ```discretise.py``` which was used for discretising the data as described in the notebook.
2. ```cluster.py``` which was used to compute and print summary statistics for the k-modes
clusters constructed in the notebook.
3. ```apriori.py``` which was used for pretty printing of the association rules generated
using apriori pruning. 

Please see the libraries for implementation details.

All tree visualisations are saved as PNG files in the same directory as ```report.ipynb``` when 
it is run.  