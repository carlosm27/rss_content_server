from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from deta import Deta
from typing import List
from feed_parser import list_of_links
import os

app = FastAPI()


load_dotenv()
PROJECT_KEY = os.environ.get("PROJECT_KEY")

deta = Deta(PROJECT_KEY)
users = deta.Base("users")


class RssLink(BaseModel):
    ChatId: int
    Links: List[str]


@app.get("/links")
def all_links():
    return users.fetch()


@app.post('/link')
def add_link(content: RssLink):
    new_content = users.put({
        'ChatId': content.ChatId,
        'links': content.Links
    })
    return new_content


@app.put('/link/{key}')
def update_content(key: str, content: RssLink):
    links = content.Links
    updates = {
        "ChatId": content.ChatId,
        "Links": users.util.append(links)
    }

    users.update(updates, key)

    return None


@app.put('/trim/{key}')
def remove_link(key: str, content: RssLink):
    ##links = content.Links
    updates = {
        "ChatId": content.ChatId,
        "Links[0]": users.util.trim()
    }
    users.update(updates, key)
    return None
