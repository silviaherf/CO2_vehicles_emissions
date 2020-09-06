import regex as re
def rename_columns(df):
    actual_col={}
    for column in df.columns:
        actual_col[column]=column.replace(r" ","_")
    df=df.rename(columns = actual_col, inplace = True)
    return df
