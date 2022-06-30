from bs4 import BeautifulSoup
import requests
import json
import lxml


def get_data():
    """Here we are trying to take the data into storage"""
    url = 'https://www.englishdom.com/skills/glossary/wordset/top-100-slov-urovnya-advanced/'

    headers = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    to_json_dict = {}

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    list_with_cards = soup.find('div', class_='word-list is-open').find_all('div', class_='item-list is-show js-word')
    for index, card in enumerate(list_with_cards, 1):   # using enumerate func to save in json with "word_id"
        word = card.find('div', class_='word-wrap').find('p', class_='word').text
        translate = card.find('div', class_='word-wrap').find('p', class_='translate').text
        to_json_dict[index] = {
            'Word': word.title(),
            'Translate': translate.title(),
            'Context': None,
            'Type': None,
        }

    with open('dictionary.json', 'w', encoding='utf-8') as f:
        json.dump(to_json_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    get_data()