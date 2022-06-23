# some python functions to used in example_notebook.ipynb

def read_multi_csv(path=""):
    import glob
    import pandas as pd
    
    all_filenames = [i for i in glob.glob(path+'*.{}'.format('csv'))]
    combined_data = pd.concat([pd.read_csv(f) for f in all_filenames ])
    return combined_data

def barplot_data(data,variable=None):
    if (variable is None):
        print('please provide a variable name!')
        return
    data.hist(variable)
    
def scatter_data(data,variable_1=None,variable_2=None):
    if (variable_1 is None) or (variable_2 is None):
        print('please provide two variable names!')
        return
    data.plot.scatter(x=variable_1,y=variable_2)
    
    

    