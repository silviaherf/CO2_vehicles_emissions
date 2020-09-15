import pandas as pd
import matplotlib.pyplot as plt

print("Hi! Which topic would you like to know about?\n-Worldwide CO2 emissions in History, \n-Different vehicle types CO2 emissions \n-Or Registered vehicles worldwide along time?")
print("Set 'world_emissions' for the first one, 'vehicles' for the second one or 'register' for the last one")
    
name=input('Please,enter the name for the DataFrame you want to open from the list above\n')

def open_df(df=name):
    """
    This function opens a DataFrame from src folder in the project.
    You must enter the name for the DataFrame you want to open from the list below
    """

    df=pd.read_csv(f'src/{name}.csv',encoding='latin-1')
    
    print(f"Here's a piece of your DataFrame:\n{df.head()}")
    
    return df


def groupping():
    """
    This function selects the information of a DataFrame a returns a graph.
    The parameters you need are:
    df- the DataFrame's name (the same as the one you selected in the open_df function)
    column- the column of the DataFrame you want to group_by the information
    a- the column you want to aggregate the sum and mean of the values
    """
    df=open_df(name)
    g=input('Please, enter the column of the DataFrame you want to group_by the information\n')
    a=input('And now enter the column you want to aggregate the sum and mean of the values\nRemember to choose a numeric column!!!')

    df_group=df.groupby(str(g)).agg({str(a):["sum","mean"]})
    return df_group



def graphicate():
    """
    This function selects the information of a DataFrame a returns a graph.
    You don't need any parameter, except of the ones the function will ask you
    """
    df=open_df(name)
    x=input('Please, enter the column of the DataFrame you want in the x axis of your graph\n')
    y=input('Please, enter the column of the DataFrame you want in the y axis of your graph\nRemember to chose a numeric column!!')
    plt.figure(figsize=(15,8))
    df.plot.bar(x=x,y=y)
    return plt.show()




