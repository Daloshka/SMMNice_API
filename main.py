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

    def vk_order_post_views(self, url:str, quantity: int) -> dict:
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
    
    def vk_order_video_views(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на видео https://vk.com/video-25182070_456247742
        params: quantity - количество просмотров   1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2338&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def vk_order_clip_views(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на клип https://vk.com/clip236054242_456241682
        params: quantity - количество просмотров   1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2339&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def vk_order_subscribers(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на пост https://vk.com/public215651944
        params: quantity - количество подписчиков  1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2459&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def tg_subscribers(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на группу https://t.me/transportkrasnoyarska
        params: quantity - количество подписчиков  1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=1506&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data
    
    def tg_fast_subscribers(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на группу https://t.me/transportkrasnoyarska
        params: quantity - количество подписчиков  1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=1542&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data

    def instagram_subscribers(self, url:str, quantity: int) -> dict:
        """
        params: url - ссылка на страницу https://www.instagram.com/your_login/
        params: quantity - количество подписчиков  1000
        return: dict - номер заказа  {'order': 66424299}
        Получение информации о заказе просмотров
        """
        order_url = self.cut_https(url)
        url = f"https://smmnice.ru/api/v2?action=add&service=2067&link={order_url}&quantity={quantity}&key={self.token}"
        response = requests.get(url)
        data = response.json()
        return data



if __name__ == "__main__":
    smm = APIManager()
       