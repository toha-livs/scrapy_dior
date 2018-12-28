import json


def get_size(response):
    text = response.xpath('/html/head/script[5]/text()').extract_first()[31:-1]
    text = json.loads(text)
    size = ''
    r = []
    try:
        r = text['CONTENT']['contents'][0]['cmsContent']['elements'][3]['variations']
    except:
        pass
    try:
        r = text['CONTENT']['cmsContent']['elements'][3]['variations']
    except:
        pass
    try:
        r = text['CONTENT']['contents'][0]['cmsContent']['elements'][4]['variations']
    except:
        pass
    if r == []:
        return 'None'
    else:
        try:
            for i in r:
                size = size + '' + str(i['detail'])[6:]
        except:
            return 'None'
    return size


def get_country(path):
    if path == 'us':
        return 'USA'
    else:
        return 'FRANCE'


def get_color(path):
    if path['variant'] == '':
        return 'None'
    for i in path['variant']:
        if i in '1234567890':
            return 'None'
        else:
            pass
    return path['variant']


def get_small_info(response):
    text = response.xpath('/html/head/script[3]/text()').extract_first()[15:-2]
    text = json.loads(text)
    return text[0]


def get_present(path):
    if path == 'inStock':
        return 'В наличии'
    else:
        return 'Нет в наличии'


def get_description(response):
    if response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div/text()').extract_first() == []:
        return 'None'
    else:
        return response.xpath('/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[1]/div/div/div/text()').extract_first()