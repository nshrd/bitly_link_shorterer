import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    link = get_arguments()
    is_bitlink = get_link_form(token, link)
    if not is_bitlink :
        new_bitlink = get_bit_link(token, link)
        if new_bitlink is None:
            print('Ссылка не найдена либо введена с ошибкой.')
        else:
            print(f'Ваш битлинк: {new_bitlink}')
    elif is_bitlink:
        total_clicks = get_clicks_info(token, link)
        if total_clicks is None:
            print('Ссылка не найдена либо введена с ошибкой.')
        else:
            print(f'Количество переходов: {total_clicks}')


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="if your link is bit.ly link - you will see total clicks statistics,\
                            otherwise you will get new bit.ly link")
    args = parser.parse_args()
    return args.link


def get_bit_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header_query = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': f'{link}'}
    response = requests.post(url, json=payload, headers=header_query)
    if not response.ok :
        return
    decoded_resp = response.json()
    bitlink = decoded_resp['link']
    return bitlink


def get_clicks_info(token, link):
    link = urlparse(link)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link.netloc}{link.path}/clicks/summary'
    header_query = {'Authorization': f'Bearer {token}'}
    payload = {'units': '-1'}
    response = requests.get(url, params=payload, headers=header_query)
    if not response.ok:
        return
    decoded_resp = response.json()
    total_clicks = decoded_resp['total_clicks']
    return total_clicks


def get_link_form(token, link):
    link = urlparse(link)
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link.netloc}{link.path}'
    header_query = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=header_query)
    return response.ok


if __name__ == '__main__':
    main()
