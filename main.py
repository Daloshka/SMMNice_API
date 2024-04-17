import requests

# СОЗДАЙТЕ ФАЙЛ config.py И ПОМЕСТИТЕ В НЕГО СВОЙ API ТОКЕН с сайта https://goo.su/zJLQac5
from config import API_TOKEN 



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

    def get_services(self) -> dict:
        """
        Получение списка услуг в JSON
        """
        url = f"https://smmnice.ru/api/v2?action=services&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data

    def order_post_views(self, url:str) -> dict:
        """
        params: url - ссылка на пост
        return: dict - 1/0 (успешно/неуспешно)
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2341&link={order_url}&quantity=100&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data


if __name__ == "__main__":
    smm = SMMNice()
    
    # TEST
    #print(smm.order_views(order_url=""))