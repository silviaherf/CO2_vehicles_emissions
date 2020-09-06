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
