import shelve

db = shelve.open('data/t0txt')

to_delete = []

WHITELIST = ['t0.vc', 'tanner', 'protospace', 'seed combinations', 'tcoins in circulation', 'pokemon trade', 'pokemon battle', 'unique in collection', '%) left.', 'telethon', 'datetime', ' +0000', 'print(', 'console.log', 'systemd', '-Iinclude', 'BOOT_IMAGE', '#endif', '/bin/bash', 'python3.', 'stdio.h', 'int main(']
BAD_WORDS = ['blogspot.com', 'livejournal.com', 'tumblr.com', 'noname.fun', 'biturl.top', 'google.com/url?q', '.ru/">', '.ru">', 'viagra']
BAD_COMBO = ['jackpot', 'casino', 'sex', 'porn', 'naked', 'xxx', 'lesbian', 'gay', 'crypto', 'pussy', 'fuck', 'cialis', 'pharmacy', 'doxycycline', 'zantac', 'ivermectin', 'drug', 'prescri', 'amateur', 'kratom', 'medicament', 'medicine', 'medication', 'lisinopril', 'pepcid', 'prilosec', 'lolita', 'bitcoin', 'ethereum', 'essay', 'professor']

LANGUAGE = [
    'fælde oversøiske får effektivitet symptomerne',
    'лучить полную консультацию нашего Менеджера также оставить заявку получение справки формы',
    'Привет нашел классный сайт про автомобили много полезной информации',
    'lekárskeho predpisu lekárni liekové interakcie lekárňach kúpiť',
    'gået årene bære мошенники пидорасы здесь обман отзывы',
    'sjukdom dysfunktion njurinfektion läser när läkemedel kända',
    'Создание дома вашей мечты это оригинальная возможность спланировать претворить жизнь нечто воистину уникальное всех отношениях',
    'Узнайте сваи винтовые для фундамента цены вытегре спспециалистовециалистов корпорации',
    'criptovaluta descuento tecnologicos portafoglio informazioni crittografia koronaviru quimioterapia',
    'ігрові автомати Казино украина отзывы киеве закрыли поездки зарубеж',
    'только недавно они вошли рынке этой продукции Предлагаем Вашему вниманию изделия',
    'Искалка интернет магазинам Без рекламы прочих прелестей современного интернета вакансии тур операторов',
    'rychlé doručení inzulín měchýře formuláře předpis během těhotenství předpis potřeby hyperkalémie kloubů možnou přijatelné',
    '第 借 錢 網 擁 有 全 台 最 多 的 借 錢 資 訊 歐 客 佬 精 品 咖 啡 遊 戲 情 報 專 業 光 碟 教 學 網 站 娛 樂 城 介 紹',
    'карта для оплаты интернете займы счет банке номер телефона монеза подпольное казино киева новости туризма операторов сыр Пинап казино',
    'Bán đến dưới giá đổi thời điểm',
    'bære strømper stråler nødvendige hænder',
    'stråling bløde antibakterielle også søvn forretningsrejse repræsenterer opnås',
    'кливленд кавальерс состав доска липа сухая москва доска дубовая обрезная сухая купить брус ясень купить новые фото кубань руна человек значение',
    'Присутствие данном присутствие больших пакгаузных комнат создало допустимым формирование постоянных поставок абсолютно всем покупателям',
    'очень интересно чичего понятно Портал котором собраны все будет полезен всем',
    'jednostavno prednosti korisnicka podrska kvalitetna',
    'antibiootikumid kasumijaotus haavandite kasutamine',
    'större säker övningar sköldkörteln Även migræne læge være træt',
    'Возможности программы компьютера новости поездок programД спасибо интересное чтиво',
    'medizinisches nutzliches gefunden',
    'يشتمل موقعنا على روابط تشعبية وتفاصيل عن مواقع خاصة بأطراف ثالثة علمًا بأنه ليس لدينا أي سيطرة على سياسات الخصوصية وممارسات الأطراف الثالثة كما أننا لسنا مسؤولين عنها',
    'psoriasi trattamento dermatite',
    'סר ט סקס ח נם',
    'ссылка Зацените Ваше мнение юмз фронтальный погрузчик или самых сексуальных моделей кредит для ип онлайн заработок на стейкинге Ботвинья Рецепт Приготовления',
    'antivirale medicijnen antivirale geneesmiddelen richten antiviraal antivirovГЅch virЕЇm',
    'заработок криптовалюте заработок стейкинге кормить почему доверяю кормам Гидра официальный сайт нем дает Заказчикам стейкинге криптовалют заработок курсы английского языка',
    'взыскание задолженности по договору поможем вернуть долг Пограничное расстройство личности',
    'ケ ー ス コ ピ シ ャ ネ ル',
]


for lang in LANGUAGE:
    BAD_COMBO += [x.strip() for x in lang.split(' ')]
BAD_COMBO = list(set(BAD_COMBO))

num_before = len(db)

for key, value in db.items():
    content = value.lower()
    skip = False

    for good_word in WHITELIST:
        if good_word in content:
            skip = True
            break

    if skip: continue

    for bad_word in BAD_WORDS:
        if bad_word in content:
            print('Deleting note', key, 'bad word:', bad_word)
            to_delete.append(key)
            skip = True
            break

    if skip: continue

    combo_hits = set()

    for bad_word in BAD_COMBO:
        if bad_word in content:
            combo_hits.add(bad_word)

    if len(combo_hits) >= 2:
        print('Deleting note', key, 'bad combo:', ', '.join(list(combo_hits)))
        to_delete.append(key)
        continue

    num_http = content.count('http')
    num_line = content.replace('\n\n', '\n').count('\n')
    link_ratio = num_http / num_line if num_line else 999

    if num_http > 7 and link_ratio > 0.75:
        print('Deleting note', key, 'links:', num_http, 'ratio:', round(link_ratio, 2))
        to_delete.append(key)
        continue

to_delete = list(set(to_delete))

print('found', len(to_delete), 'notes to delete')

for key in to_delete:
    del db[key]

#import random
#while True:
#    note_id = random.choice(to_delete)
#    note = db[note_id]
#
#    print()
#    print('===================================================')
#    print()
#    print(note)
#    input()

print('done.')
