from model.rss_link_model import RssLink, users


def add_link(content: RssLink):
    new_content = users.put({
        'ChatId': content.ChatId,
        'links': content.Links
    })
    return new_content


def get_key(key:str):
    user_info = users.get(key)
    return user_info


def append_content(key: str, content: RssLink):
    links = content.Links
    updates = {
        "ChatId": content.ChatId,
        "Links": users.util.append(links)
    }

    users.update(updates, key)

    return None


def remove_link(key: str, content: RssLink):
    ##links = content.Links
    updates = {
        "ChatId": content.ChatId,
        "Links[0]": users.util.trim()
    }
    users.update(updates, key)
    return None


def get_link(link: str):
    link = users.get(link)
    return link