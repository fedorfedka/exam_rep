import pandas as pd


def get_rows_from_scv(file_name :str, row_count: str) -> str:
    file = pd.read_csv(file_name)
    
    if row_count == '*':
        return file.head().to_string()

    else:
        row_count = int(row_count)
        if row_count > 0:
            return file.head(row_count).to_string()

        elif row_count < 0:
            return file.tail(abs(row_count)).to_string()
        
    return 'None'


def search_rows_from_scv(file_name :str, value) -> str:
    file = pd.read_csv(file_name)
    for column in file:
        if (file.loc[file[column] == value]).empty == False:
            return file.loc[file[column] == value].to_string()

    return 'None'
