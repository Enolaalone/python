import jieba
from pyecharts.charts import Pie, Page

ten_same_2021 = {}
ten_same_2022 = {}
five_difference = {}


def jieba_analyse(name):
    report_0 = []
    report_1 = []
    words = {}
    words_ten = {}

    with open(f'{name}.txt', 'r', encoding='utf-8') as f:
        report_0 = f.readlines()
        for i in report_0:
            if i != '\n':
                i = i.strip('\n')
                report_1.append(i)
    for sentence in report_1:
        list = jieba.cut(sentence, cut_all=True)
        for word in list:
            if len(word) >= 2:
                words[word] = words.get(word, 0) + 1

    word_order = sorted(words.items(), key=lambda x: (x[1], x[0]), reverse=True)

    for i in range(10):
        words_ten[word_order[i][0]] = word_order[i][1]
    print(words_ten)
    return words_ten


report_2021 = jieba_analyse('政府工作报告2021')
report_2022 = jieba_analyse('政府工作报告2022')

for key in report_2021:
    if key in report_2022:
        ten_same_2021[key] = report_2021[key]
        ten_same_2022[key] = report_2022[key]

list_1 = list(report_2021)
list_2 = list(report_2022)
list_2021 = []
list_2022 = []
for i in range(5):
    list_2021.append(list_1[i])
    list_2022.append(list_2[i])

for i in range(5):
    if list_2021[i] not in list_2022:
        five_difference[list_2021[i]] = report_2021[list_2021[i]]
    if list_2022[i] not in list_2021:
        five_difference[list_2022[i]] = report_2022[list_2022[i]]
print(five_difference)

page = Page()
pie0 = Pie().add('前十相同2021', [ten_same_2021 for ten_same_2021 in zip(ten_same_2021.keys(), ten_same_2021.values())])
pie1 = Pie().add('前十相同2022', [ten_same_2022 for ten_same_2022 in zip(ten_same_2022.keys(), ten_same_2022.values())])
pie3 = Pie().add('前五不同',
                 [five_difference for five_difference in zip(five_difference.keys(), five_difference.values())])
page.add(pie0, pie1, pie3).render('年度报告数据分析.html')
