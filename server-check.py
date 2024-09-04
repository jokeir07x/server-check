import requests
from multiprocessing.pool import ThreadPool
from urllib.parse import urlparse
import click

def check_server(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            server_info = response.headers.get('Server', 'Unknown')
            if server_info.startswith('Apache'):
                return f"{url} | {server_info}"
            else:
                return None
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def save_result(result):
    if result:
        with open('Jokeir07x.txt', 'a') as file:
            file.write(f"- > {result}\n")

def process_url(url):
    if not urlparse(url).scheme:
        url = "http://" + url
    result = check_server(url)
    if result:
        click.echo(f"{url} -> {click.style('OK', fg='green')}")
        save_result(result)
    else:
        click.echo(f"{url} -> {click.style('Unknown', fg='red')}")

def main():
    print("MASS LOOKUP HTTP SERVER BY @Jokeir0 7x | CHANNEL: https://t.me/jokeir7x0")
    file_name = input("Jokeir07x-lista?: ")
    with open(file_name, 'r') as file:
        urls = file.read().splitlines()

    pool = ThreadPool(5)
    pool.map(process_url, urls)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
