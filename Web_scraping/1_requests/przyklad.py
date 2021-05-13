import requests


def run():
    response = requests.get("https://joemonster.org/")
    print(response.status_code)
    print(response.ok)

    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    run()