```python
import mysql.connector
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-1-9cd6224ba968> in <module>
    ----> 1 import mysql.connector
    

    ModuleNotFoundError: No module named 'mysql'



```python
conda install -c anaconda mysql-connector-python

```

    Collecting package metadata (current_repodata.json): ...working... done
    Note: you may need to restart the kernel to use updated packages.
    Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.
    Solving environment: ...working... failed with repodata from current_repodata.json, will retry with next repodata source.
    Collecting package metadata (repodata.json): ...working... done
    Solving environment: ...working... failed with initial frozen solve. Retrying with flexible solve.
    Solving environment: ...working... 
    Found conflicts! Looking for incompatible packages.
    This can take several minutes.  Press CTRL-C to abort.
    failed
    
    

    
    Building graph of deps:   0%|          | 0/4 [00:00<?, ?it/s]
    Examining @/win-64::__archspec==1=x86_64:   0%|          | 0/4 [00:00<?, ?it/s]
    Examining @/win-64::__win==0=0:  25%|##5       | 1/4 [00:00<?, ?it/s]          
    Examining mysql-connector-python:  50%|#####     | 2/4 [00:00<?, ?it/s]
    Examining python=3.8:  75%|#######5  | 3/4 [00:00<00:00,  6.21it/s]    
    Examining python=3.8: 100%|##########| 4/4 [00:00<00:00,  8.27it/s]
                                                                       
    
    Determining conflicts:   0%|          | 0/4 [00:00<?, ?it/s]
    Examining conflict for mysql-connector-python python:   0%|          | 0/4 [00:00<?, ?it/s]
                                                                                               
    
    UnsatisfiableError: The following specifications were found
    to be incompatible with the existing python installation in your environment:
    
    Specifications:
    
      - mysql-connector-python -> python[version='>=3.5,<3.6.0a0|>=3.6,<3.7.0a0|>=3.7,<3.8.0a0']
    
    Your python: python=3.8
    
    If python is on the left-most side of the chain, that's the version you've asked for.
    When python appears to the right, that indicates that the thing on the left is somehow
    not available for the python version you are constrained to. Note that conda will not
    change your python version to a different minor version unless you explicitly specify
    that.
    
    
    
    


```python
import mysql.connector
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-3-9cd6224ba968> in <module>
    ----> 1 import mysql.connector
    

    ModuleNotFoundError: No module named 'mysql'



```python

```
