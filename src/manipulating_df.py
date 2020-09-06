
import pandas as pd

def export_cvs(df):
    """ This function export a cvs file to src folder in my project.
    To use it, it needs one parameter:
    df:the DataFrame we are willing to export to cvs
    """
    name=input('Please, enter the name for the cvs file you want to export')
    df.to_csv(f"src/{name}.csv",index = False)
    return f"{name} has been exported to cvs file"

def open_cvs():
    """ This function opens a cvs file from src folder in my project. and saves it into a pandas DataFrame
    No parameters are needed, except of the name the function will ask you
    """
    name=input('Please, enter the name for the cvs file you want to open without extension:\n')
    

    return pd.read_csv(f'src/{name}.csv',encoding='latin-1')
