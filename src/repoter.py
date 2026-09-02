class DataFrameReporter:

# Инициализация конструктора с параметрами по умолчанию
    def __init__(self, float_format = '0.05f', percent_format = '0.02%', include_all = False):
        self.float_format = float_format 
        self.percent_format = percent_format
        self.include_all = include_all

#  Создание метода show_report для вывода базовой информации о датасете
    def show_report(self, df, title = None):
        if title != None:
            print(title)
        print(f'Количество столбцов: {df.shape[1]}')
        print(f'Количество строк: {df.shape[0]}')
        print(f'Количество дубликатов: {df.duplicated().sum()}')
        print(f'Доля дубликатов: {format(df.duplicated().mean(), self.percent_format)}')

        # Добавление вывода метода '.describe()',
        # если пользователь передал в переменную экземпляра параметр "include_all = True"
        if self.include_all:
            print(df.describe(include='all'))
        else:
            print(df.describe(include=None))