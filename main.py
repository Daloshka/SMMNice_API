import requests

# ПОМЕСТИТЕ В config.py СВОЙ API_TOKEN с сайта https://goo.su/zJLQac5
from config import API_TOKEN 



class APIManager():
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

    def order_post_views(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на пост https://vk.com/wall-213538534_86
        params: quantity - количество просмотров  1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2341&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def order_video_views(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на пост https://vk.com/wall-213538534_86
        params: quantity - количество просмотров   1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2338&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data


if __name__ == "__main__":
    smm = APIManager()
    