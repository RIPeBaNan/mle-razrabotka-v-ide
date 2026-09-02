# MLE: Разработка в IDE
Учебный проект для отработки базовых навыков разработки в IDE: структурирование Python-проекта, управление виртуальным окружением, оформление кода по стандартам и реализация модуля первичного разведочного анализа данных (EDA) табличных датасетов.

---

## О проекте

Основная цель репозитория — переход от ноутбуков (Jupyter Notebook) к модульной разработке скриптов. В проекте реализован класс DataFrameReporter, автоматизирующий сбор базовой статистики по переданному датафрейму.

**Решаемые задачи:**
* Подсчет размерности (строки, столбцы);
* Поиск дубликатов (абсолютное значение и доля);
* Поиск пропусков по всей таблице;
* Формирование сводки описательной статистики (.describe()) с гибким управлением числовыми форматами.

---

## Структура проекта

```text
mle-razrabotka-v-ide/
├── data/
│   └── payments.csv        # Пример датасета для анализа
├── src/
│   ├── repoter.py          # Модуль с классом DataFrameReporter
│   └── requirements.txt    # Список зависимостей
├── .gitignore              # Игнорируемые файлы (venv, кэш, системные файлы)
├── main.py                 # Главная точка входа для запуска анализа
└── README.md               # Документация проекта
```

---

## Установка и настройка окружения
1. Клонируйте репозиторий:
```bash
git clone [https://github.com/RIPeBaNan/mle-razrabotka-v-ide.git](https://github.com/RIPeBaNan/mle-razrabotka-v-ide.git)
cd mle-razrabotka-v-ide
```
2. Создайте и активируйте виртуальное окружение:
* Windows (PowerShell):
```powershell
py -3.12 -m venv main_venv
.\main_venv\Scripts\Activate.ps1
```
* macOS / Linux:
```bash
python3.12 -m venv main_venv
source main_venv/bin/activate
```
3. Установите зависимости:
```pip3 install -r requirements.txt```

---

## Запуск
Для выполнения отчета по данным запустите скрипт main.py из корневой директории проекта:
```python main.py```

---

## Пример использования модуля
Класс DataFrameReporter можно переиспользовать в любых сторонних скриптах:
```python
import pandas as pd
from src.repoter import DataFrameReporter

# Загрузка данных
df = pd.read_csv('data/payments.csv')

# Инициализация репортера с пользовательским форматом
reporter = DataFrameReporter(
    float_format='0.03f', 
    percent_format='0.02%', 
    include_all=True
)

# Генерация отчета в консоль
reporter.show_report(df, title='Отчет по транзакциям')
```

---

### Cтек технологий
* Python 3.10+
* Pandas — обработка и агрегация табличных данных
* Virtualenv / venv — изолированное окружение разработки