import requests


def run():
    try:
        response = requests.get("https://infoshareacademy.com/")
    except requests.RequestException as error:
        print(f"Błąd połączenia: {error}")
        return
    try:
        response.raise_for_status()
    except requests.HTTPError as error:
        print(f"Żądanie zakończone niepowodzeniem: {error}")
        return
    print(response.text)


if __name__ == '__main__':
    run()