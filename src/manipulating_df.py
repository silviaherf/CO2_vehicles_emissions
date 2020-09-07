
import pandas as pd

def export_cvs(df):
    """ 
    This function export a cvs file to src folder in my project.
    To use it, it needs one parameter:
    df:the DataFrame we are willing to export to cvs
    """
    name=input('Please, enter the name for the cvs file you want to export')
    df.to_csv(f"src/{name}.csv",index = False)
    return f"{name} has been exported to cvs file"

def open_cvs():
    """ 
    This function opens a cvs file from src folder in my project, in a shape of a pandas DataFrame
    No parameters are needed, except of the name and the folder the function will ask you
    """
    folder=input("Please, enter the folder where your cvs file is saved:\n")
    name=input('Please, enter the name for the cvs file you want to open without extension:\n')
    

    return pd.read_csv(f'{folder}/{name}.csv',encoding='latin-1')

def open_df():
    """ 
    This function opens a DataFrame from src folder in my project. 
    No parameters are needed, except of the name the function will ask you
    """
    print("Hi! Which topic would you like to know about?\nWorldwide CO2 emissions in History, Different vehicle types CO2 emissions or Registered vehicles worldwide along time?")
    print(" Set 'world_emission' for the first one, 'vehicles' for the second one or 'register' for the last one")
    name=input('Please, enter the name for the DataFrame you want to open without extension:\n')
    

    return pd.read_csv(f'src/{name}.csv',encoding='latin-1')
