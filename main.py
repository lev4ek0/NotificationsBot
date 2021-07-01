# coding=utf-8
import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType


session = requests.Session()
vk_session = vk_api.VkApi(token="token")
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


users = [99446331]


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user and event.user_id not in users:
            vk.messages.send(
                user_id=event.user_id,
                message="Тебе только что ответил бот. Прямо сейчас я занят. Если что-то важное, то напиши \"/важное\", мне придет уведомление",
                random_id=0,
            )
            users.append(event.user_id)
        if event.from_user and event.text == "/важное":
            vk.messages.send(
                user_id=99446331,
                message="Тебе написали что-то важное",
                random_id=0,
            )
