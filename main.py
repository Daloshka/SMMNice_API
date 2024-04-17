import requests

from config import API_TOKEN

# API endpoint

class SMMNice():
    def __init__(self):
        self.token = API_TOKEN

    def cut_https(self, url):
        if url.startswith("https://"):
            return url[8:]
        elif url.startswith("http://"):
            return url[7:]
        else:
            return url

    def get_services(self):
        url = f"https://smmnice.ru/api/v2?action=services&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data

    def order_views(self, url):
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2341&link={order_url}&quantity=100&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data


if __name__ == "__main__":
    smm = SMMNice()
    print(smm.cut_https("http://google.com"))
    #print(smm.order_views(order_url=""))