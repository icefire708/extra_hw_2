"""
Дополнительное задание.

В папке data вы найдее несколько файлов с составами фондов в формате .csv
Каждая строка это ценная бумага/торговый инструмент, столбец weight это какой процент от всего фонда занимает эта бумага

Нужно вывести в консоль:
1. Название фонда
2. Дата отчета (подсказка, дата отчета содержится в конце названия файла, например 21052021)
3. Вывести для каждого отчета 10 самых крупных компонентов (Отсортировать по weight)
4. Полностью ли заполнен фаил (сумма весов в каждом файле равна 100%)

Потом:
Сохранить все отчеты в 1 фаил top_ten_report.csv:
1. Нужны только 10 крупнейших компонентов
2. Если для фонда есть более свежие данные, старые данные не сохранять в финальный отчет
4. Столбцы: date, fund_name, currency, weight

Подсказка/вариант как получить имена всех файлов.
from pathlib import Path

reports = Path('./data').glob('*.csv')
for file in reports:
    print(report.name)

"""
import csv
from glob import glob


def process_data() -> None:
    reports = glob("data/*.csv")
    for index, file_name in enumerate(reports):
        print(f'Файл отчёта №{index + 1}: {file_name}')
        strip_file_name = file_name[len('data/'):-len('.csv')]
        file_name_parts = strip_file_name.split('_')
        fund_name = ' '.join(file_name_parts[:-2])
        print(f'1) Название фонда: {fund_name}')
        report_date = file_name_parts[-1]
        # свято верю, что даты с ведущим нулём 07052020
        print(f'2) Дата отчёта: {report_date[:2]}-{report_date[2:4]}-{report_date[-4:]}')
        sum_ = 0
        with open(file_name, 'r') as f:
            fields = ['Account Number', 'Account Name', 'ISIN', 'Trading Currency', 'Weight']
            reader = csv.DictReader(f, fields, delimiter=',')

        print('=' * 15)
if __name__ == '__main__':
    process_data()
