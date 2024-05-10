import vk_api

token = ""

session = vk_api.VkApi(token=token)
vk = session.get_api()


def friends(page):
    friends_list = []  # [[user_name, id_user]]
    for i in range(page * 10 - 10, page * 10):
        friends = (vk.friends.get(fields=True, order="hints")).get("items")
        friends_list.append([f'{friends[i].get("first_name")} {friends[i].get("last_name")}', friends[i].get("id")])
    return friends_list


def chat_list():
    chat_list = []  # [[user_name, id_user. last_message[:20]]]
    chat = vk.messages.getConversations()

    #group
    title_group = chat.get("items")[0].get("conversation").get("chat_settings").get("title")

    # chat with users
    for i in range(len(chat.get("items"))):
        # chats with users
        if chat.get("items")[i].get("conversation").get("peer").get("type") == "user":
            id_user = (chat.get("items")[i].get("conversation").get("peer").get("local_id"))
            title_user = f"{vk.users.get(user_id=id_user)[0].get('first_name')} {vk.users.get(user_id=id_user)[0].get('last_name')}"
            last_message = chat.get("items")[i].get("last_message").get("text")

            if len(last_message) > 50:
                last_message = last_message[:50]

            if len(chat.get("items")[i].get("last_message").get("attachments")) != 0:
                if (chat.get("items")[i].get("last_message").get("attachments")[0].get("type") == "video"):
                    last_message = "Видео"
                elif (chat.get("items")[i].get("last_message").get("attachments")[0].get("type")== "link"):
                    last_message = "Ссылка"
                elif (chat.get("items")[i].get("last_message").get("attachments")[0].get("type") == "doc"):
                    last_message = "Файл"
                elif (chat.get("items")[i].get("last_message").get("attachments")[0].get("type")== "audio"):
                    last_message= "Аудиозапись"

            chat_list.append([title_user, id_user, last_message.rstrip("\n")])

        # group chats
        elif chat.get("items")[i].get("conversation").get("peer").get("type") == "chat":
            title_group = (chat.get("items")[i].get("conversation").get("chat_settings").get("title"))
            last_message = chat.get("items")[i].get("last_message").get("text")

            if len(last_message) > 50:
                last_message = last_message[:50]

            if len(chat.get("items")[0].get("last_message").get("attachments")) != 0:
                if (chat.get("items")[0].get("last_message").get("attachments")[0].get("type") == "video"):
                    last_message = "Видео"
                elif (chat.get("items")[0].get("last_message").get("attachments")[0].get("type")== "link"):
                    last_message = "Ссылка"
                elif (chat.get("items")[0].get("last_message").get("attachments")[0].get("type") == "doc"):
                    last_message = "Файл"
                elif (chat.get("items")[0].get("last_message").get("attachments")[0].get("type")== "audio"):
                    last_message = "Аудиозапись"

            chat_list.append([title_group, "id_group", last_message.rstrip("\n")])
    
    return chat_list

