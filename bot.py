import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll
from db.registr import registr
import random
import json
import time
from db.db import Bot

db = Bot()
token = "5d3a98c4a2391ecc5bbd14613f886e687d16e7354e9ad2d2485057428015a7371f6bbf790372f1157f290"
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def get_name(user_id):
    data = vk.users.get(user_id=event.user_id, access_token=token, v=5.103)
    return data['response']


keyboard = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Создать"
                },
                "color": "primary"
            }]]}

keyboardn1 = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Парень"
                },
                "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Девушка"
                },
                "color": "primary"
            }]]}

keyboardn2 = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Парня"
                },
                "color": "primary"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Девушку"
                },
                "color": "primary"
            }]]}

keyboard3 = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Просмотр"
                },
                "color": "primary"
            }]]}

keyboard4 = {
    "one_time": False,
    "buttons": [
        [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "♡"
                },
                "color": "positive"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "👎🏻"
                },
                "color": "negative"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "💤"
                },
                "color": "primary"
            }]]}

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_chat or event.from_user:
                response = event.text.lower()
                if response == "начать":
                    db.reg(event.user_id)
                    vk.messages.send(user_id=event.user_id, message="Создадим анкету", keyboard=json.dumps(keyboard, ensure_ascii=False), random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "просмотр":
                    vk.messages.send(user_id=event.user_id, message=f"Ваше имя: {db.get_username(event.user_id, token)}\n"
                                                                    f"Ваш пол: {db.get_anketa(event.user_id)['gender']} \n"
                                                                    f"Вы ищите: {db.get_anketa(event.user_id)['poisk']} \n"
                                                                    f"Ваша фотография: ",
                                                                    keyboard=json.dumps(keyboard4, ensure_ascii=False),
                                                                    random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "создать":
                    vk.messages.send(user_id=event.user_id, message="Введите ваш пол", keyboard=json.dumps(keyboardn1, ensure_ascii=False), random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "девушка":
                    db.insert_anketa_w(event.user_id)
                    vk.messages.send(user_id=event.user_id, message="Кого хотите найти?", keyboard=json.dumps(keyboardn2, ensure_ascii=False), random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "парень":
                    db.insert_anketa_m(event.user_id)
                    vk.messages.send(user_id=event.user_id, message="Кого хотите найти?", keyboard=json.dumps(keyboardn2, ensure_ascii=False), random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "девушку":
                    db.insert_anketa_pw(event.user_id)
                    vk.messages.send(user_id=event.user_id, message="Анкета создана", keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "парня":
                    db.insert_anketa_pm(event.user_id)
                    vk.messages.send(user_id=event.user_id, message="Анкета создана", keyboard=json.dumps(keyboard3, ensure_ascii=False), random_id=random.randint(1, 2147483647))

                elif response.split()[0] == "♡":
                    if db.get_profile(event.user_id):
                        vk.messages.send(user_id=event.user_id, message=f"Посмотрите кого мы нашли\n"
                                                                        f"Его(Ее) имя: {db.get_profile(event.user_id)['name']}\n"
                                                                        f"Его(Ее) пол: {db.get_profile(event.user_id)['gender']}\n"
                                                                        f"Его(Ее) поиск: {db.get_profile(event.user_id)['poisk']}\n",
                                                                        keyboard=json.dumps(keyboard4, ensure_ascii=False),
                                                                        random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "👎🏻":
                    vk.messages.send(user_id=event.user_id, message="Злой(-ая) вы",
                                     keyboard=json.dumps(keyboard4, ensure_ascii=False),
                                     random_id=random.randint(1, 2147483647))
                elif response.split()[0] == "💤":
                    vk.messages.send(user_id=event.user_id, message="Ждем вас снова",
                                     keyboard=json.dumps(keyboard4, ensure_ascii=False),
                                     random_id=random.randint(1, 2147483647))
                '''else:
                    vk.messages.send(user_id=event.user_id, message="Отъебись, эльфийский не пониаю", random_id=random.randint(1, 2147483647))'''
