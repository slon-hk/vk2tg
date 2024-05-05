import vk_api

token = "vk1.a.Uc0EN3_PHjlq5Nwb6uIsKQgvphAG0SSGKXg2i18kgYBEe4v8g5NrL27rvrTp5YhFLQb5U2Ka-Th87Get3E2yzKxKLCEAXrDnc_csLAV2s9azbfPjzSkzUPYZaZlg7wdcoLRUovQdsk_Rd85omLhRNBzWHpFPoxiUcekV4SgaH4oB73jvsgScNgzRUZrfEhEPcgFiZFja908n5aCT9zP6Eg"

session = vk_api.VkApi(token=token)
vk = session.get_api()


def send(msg):
    # vk.messages.send(user_id=499729999, message=msg, random_id=1)
    print(vk.messages.getDialogs(unread=1, unanswered=1))


def friends(page):
    friends_list = []
    for i in range(page * 10 - 10, page * 10):
        friends = (vk.friends.get(fields=True, order="hints")).get("items")
        friends_list.append(
            [
                friends[i].get("first_name"),
                friends[i].get("last_name"),
                friends[i].get("id"),
            ]
        )
    return friends_list


def chat(page):
    chat_list = []
    chat = vk.messages.getDialogs()
    count = chat.get("count")
    chat = chat.get("items")
    for i in range(chat.get("count")):
        name = vk.friends.search(user_id="1")
    print(chat)


chat(1)
