import regex as re
def rename_columns(df):
    """ 
    This function checks the name of the columns in a DataFrame and replace blank spaces with "_".
    The only argument needed is df:the DataFrame
    """
    actual_col={}
    for column in df.columns:
        actual_col[column]=column.replace(r" ","_")
    df=df.rename(columns = actual_col, inplace = True)
    return df

def rounding(df):
    """
    This function rounds every numerical column in a DataFrame to 2 decimals.
    The only argument needed is df:the DataFrame
    """
    for column in df.select_dtypes(include=['int','float']).columns:
        df[column]=df[column].map(lambda x:round(x,2))
    return df

def white_spaces(df,column):
    """
    This function removes every white space in the selected column in a DataFrame. It changes the type of 
    values to integer, if it still keeps as string.
    The two arguments needed are:
    df:the DataFrame
    column:the column from the dataFrame as a string
    """
    if type(column[0])== str:
        df[column]=df[column].map(lambda x: "".join(x.split()))
    if type(column[0])!= int and type(column[0])!= float:
        df[column]=df[column].map(lambda x: int(x))
    return df   
