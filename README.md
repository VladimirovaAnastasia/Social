# Инструмент для публикации постов в соцсетях 

Скрипт публикует ваш текст и фотографию для поста в группе [ВКонтакте](https://vk.com/), группе [Facebook](https://www.facebook.com/) и канале [Telegram](https://tlgrm.ru/). 

## Как запустить
 Устанавливаем необходимые библиотеки
 ```pip install requirements.txt```.
 
 Для работы скрипта необходимы ваши данные от аккаунтов социальных сетей. Чтобы их указать в папке со скриптом необходимо создать файл с именем `.env`. Открыв его с помощью любого текстового редактора, необходимо указать данные в следующем формате (без кавычек):
 ```
VK_LOGIN = your_vk_login
VK_TOKEN = your_vk_token
TG_TOKEN = your_tg_token

TG_CHAT_ID = your_tg_chat_id
VK_ALBUM_ID = your_vk_album_id
VK_GROUP_ID = your_vk_group_id

FB_TOKEN = your_fb_token
FB_GROUP_ID = your_fb_group_id
```

Как получить данные параметры: 

`VK_LOGIN` - логин от страницы ВКонтакте,

`VK_TOKEN` - [инструкция](https://devman.org/qna/63/kak-poluchit-token-polzovatelja-dlja-vkontakte/), 

`TG_TOKEN` - [инструкция](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/), 

`TG_CHAT_ID` - ссылка на канал, например: @dvmn_flood, 

`VK_ALBUM_ID` - если зайти на страницу с альбомом, в адресной строке будет ссылка вида: https://vk.com/public{group_id}?z=album-{group_id}_{album_id},

`VK_GROUP_ID` - [инструкция](https://regvk.com/id/),

`FB_TOKEN` - [инструкция](https://developers.facebook.com/docs/graph-api/explorer/),

`FB_GROUP_ID` - id группы (взять из ссылки на неё).

 Запускаем скрипт командой 
 ```
 python script.py POST_IMG POST_TEXT
 ```
  
 `POST_IMG` - путь до картинки в папке img (обязательный параметр), для теста можно использовать ```img/test.jpg ```
 
 `POST_TEXT` - текст поста (обязательный параметр).
 
 
## Цель проекта
 Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/) 
