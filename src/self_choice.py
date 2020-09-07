def open_df():
    """
    This function opens a DataFrame from src folder in the project.
    No parameters are needed, except of the name the function will ask you
    Don't forget to add .head() please!
    """
    print("Hi! Which topic would you like to know about?\n-Worldwide CO2 emissions in History, \n-Different vehicle types CO2 emissions \n-Or Registered vehicles worldwide along time?")
    print("Set 'world_emissions' for the first one, 'vehicles' for the second one or 'register' for the last one")
    
    name=input('Please, enter the name for the DataFrame you want to open from the list above:\n')
    

    return pd.read_csv(f'src/{name}.csv',encoding='latin-1')
