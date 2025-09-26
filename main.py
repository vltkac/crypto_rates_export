import argparse, requests, csv, json


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--export_format', type=str, default='json', help='new file extension')
    parser.add_argument('--new_file_name', type=str, default='rates', help='new file name')

    return parser.parse_args()


def main():
    arguments = get_args()

    try:
        response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1')
        response.raise_for_status()

        data = response.json()

        all_currencies = [{'currency': currency['name'],
                           'symbol': currency['symbol'],
                           'current_price_in_usd': currency['current_price'],
                           'market_capitalization_in_usd': currency['market_cap'],
                           'highest_price_within_24_hours_in_usd': currency['high_24h'],
                           'lowest_price_within_24_hours_in_usd': currency['low_24h']}
                          for currency in data]

        if arguments.export_format == 'json':
            with open(arguments.new_file_name + '.json', 'w', encoding='utf-8') as f:
                json.dump(all_currencies, f, indent=4, ensure_ascii=False)

            print(f"Data saved to {arguments.new_file_name}.{arguments.export_format}")
        elif arguments.export_format == 'csv':
            with open(arguments.new_file_name + '.csv', 'w', encoding='utf-8', newline='') as f:
                header = ('currency', 'symbol', 'current_price_in_usd', 'market_capitalization_in_usd', 'highest_price_within_24_hours_in_usd', 'lowest_price_within_24_hours_in_usd')

                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()

                for currency in all_currencies:
                    writer.writerow(currency)

            print(f"Data saved to {arguments.new_file_name}.{arguments.export_format}")
        else:
            print('Please insert JSON or CSV format in the parameter.')


    except requests.exceptions.RequestException as err:
        print(f'Network error occurred: {err}')


if __name__ == '__main__':
    main()