import pandas as pd
from src.repoter import DataFrameReporter

def main():

    # Выгружаем датафрейм в df
    df = pd.read_csv('data/payments.csv')

    # Инициализируем класс DataFrameReporter в переменную base_info
    # и задаем include_all=True для запуска условия с методом .describe()
    base_csv = DataFrameReporter(include_all=True)

    # Применяем метод show_report()
    base_csv.show_report(df, 'Таблица платежей')

if __name__ == '__main__':
    main()