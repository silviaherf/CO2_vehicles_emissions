def export_cvs(df):
    """ This function export a cvs file to src folder in my project.
    To use it, it needs two parameters:
    df:the DataFrame we are willing to export to cvs
    name:the name for the cvs file
    """
    name=input('Please, enter the name for the cvs file you want to export')
    df.to_csv(f"src/{name}.csv")
    return f"{name} has been exported to cvs file"