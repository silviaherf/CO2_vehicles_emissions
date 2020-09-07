
import pandas as pd

def export_cvs(df):
    """ 
    This function export a cvs file to src folder in the project.
    To use it, it needs one parameter:
    df:the DataFrame we are willing to export to cvs
    """
    name=input('Please, enter the name for the cvs file you want to export')
    df.to_csv(f"src/{name}.csv",index = False)
    return f"{name} has been exported to cvs file"

def open_cvs():
    """ 
    This function opens a cvs file from src folder in the project, in a shape of a pandas DataFrame
    No parameters are needed, except of the name and the folder the function will ask you
    """
    folder=input("Please, enter the folder where your cvs file is saved:\n")
    name=input('Please, enter the name for the cvs file you want to open without extension:\n')
    

    return pd.read_csv(f'{folder}/{name}.csv',encoding='latin-1')

