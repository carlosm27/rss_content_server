from fastapi import FastAPI, HTTPException


from model.rss_link_model import RssLink, users

from service.rss_content import get_key, add_link, append_content

app = FastAPI()


@app.get("/links")
def all_links():
    return users.fetch()


@app.get("/link/{key}")
def get_user_links(key: str):
    user = get_key(key)
    if not user:
        raise HTTPException(status_code=404, detail="Key not found")

    return user


@app.post('/link')
def add_content(content: RssLink):
    new_content = add_link(content)
    return new_content


@app.put('/link/{key}')
def update_content(key: str, content: RssLink):

    user = get_key(key)
    if not user:
        raise HTTPException(status_code=404, detail="Key not found")

    user_links = user['Links']
    content_link = content.Links[0]
    for index in range(len(user_links)):
        if user_links[index] == content_link:
            return {"message": "Link already exists"}

    link_to_append = append_content(key, content)
    return link_to_append


@app.put('/trim/{key}')
def remove_link(key: str, content: RssLink):
    user = get_key(key)
    if not user:
        raise HTTPException(status_code=404, detail="Key not found")
    # links = content.Links

    updates = {
        "ChatId": content.ChatId,
        "Links[0]": users.util.trim()
    }
    users.update(updates, key)
    return None
