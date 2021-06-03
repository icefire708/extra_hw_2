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
from os import write


def process_data() -> None:
    reports = glob("data/*.csv")
    to_top_ten_components = {}
    for index, file_name in enumerate(reports):
        print(f'Файл отчёта №{index + 1}: {file_name}')
        strip_file_name = file_name[len('data/'):-len('.csv')]
        file_name_parts = strip_file_name.split('_')
        fund_name = ' '.join(file_name_parts[:-2])
        print(f'1) Название фонда: {fund_name}')
        report_date = file_name_parts[-1]
        print(f'2) Дата отчёта: {report_date[:2]}-{report_date[2:4]}-{report_date[-4:]}')
        sum_ = 0
        components = []
        with open(file_name, 'r') as f:            
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                weight = int(row['Weight'].replace('%', '').replace(',', ''))
                components.append((report_date, fund_name, row['Trading Currency'], weight/100))
                sum_ += weight
        sum_ /= 100
        components.sort(key=lambda x: x[3], reverse=True)
        components = components[:10]
        print('3) 10 самых крупных компонентов:')
        for component in components:
            print(*component, sep=', ', end='')
            print('%')
        if sum_ == 100:
            print('4) Файл заполнен полностью (на 100%)')
        else:
            print(f'4) Файл заполнен не полностью (на {sum_}%)')
        print('=' * 15)
        to_top_ten_components[fund_name] = components
    top_ten_components = []
    for value in to_top_ten_components.values():
        top_ten_components.extend(value)
    top_ten_components.sort(key=lambda x: x[3], reverse=True)
    top_ten_components = top_ten_components[:10]
    with open('top_ten_report.csv', 'w', encoding='UTF-8', newline='') as f:
        fields = ['date', 'fund_name', 'currency', 'weight']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for component in top_ten_components:
            writer.writerow(dict(zip(fields, component))) 

if __name__ == '__main__':
    process_data()
