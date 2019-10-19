import csv
from django.shortcuts import render
from django.template.defaulttags import register

data = []
def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for line in reader:
            data.append({'Год': line["Год"], 'Январь': line["Янв"], 'Февраль': line["Фев"], 'Март': line["Мар"],
                         'Апрель': line["Апр"], 'Май': line["Май"], 'Июнь': line["Июн"], 'Июль': line["Июл"],
                         'Август': line["Авг"], 'Сентябрь': line["Сен"], 'Октябрь': line["Окт"], 'Ноябрь': line["Ноя"],
                         'Декабрь': line["Дек"], 'Всего': line["Суммарная"]})
    list_data = []
    for item in data:
        dict_data = {}
        for key in item:
            if key != 'Год':
                if item[key] != '':
                    dict_data.update({key: float(item[key])})
                else:
                    dict_data.update({key: '-'})
            else:
                dict_data.update({key: item[key]})
        list_data.append(dict_data)

    context = {'inflation': list_data}

    return render(request, template_name,
                  context)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)