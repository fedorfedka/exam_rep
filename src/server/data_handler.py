import pandas as pd

# получение строк таблицы из .csv документа
def get_rows_from_scv(file_name :str, row_count: str) -> str:

    # чтение файла
    file = pd.read_csv(file_name)
    
    # в случае если будет введено select *
    if row_count == '*':
        return file.head().to_string()

    # в противном случае выполняется код ниже
    else:

        # в случае если нужно вывести строки от нуля
        row_count = int(row_count)
        if row_count > 0:
            return file.head(row_count).to_string()

        # в случае если нужно вывести строки с конца
        elif row_count < 0:
            return file.tail(abs(row_count)).to_string()
        
    # в случае нуля и друких вариантов ничего
    return 'None'


# поиск строк с определенными значениями
def search_rows_from_scv(file_name :str, value) -> str:

    # чтение файла
    file = pd.read_csv(file_name)

    # цикл для проверки столбца в которой будет строка с нужными данными
    for column in file:
        if (file.loc[file[column] == value]).empty == False:

            # вернутся только те строчки в которые есть нужное значение
            return file.loc[file[column] == value].to_string()

    # если ничего нет выведем None
    return 'None'
