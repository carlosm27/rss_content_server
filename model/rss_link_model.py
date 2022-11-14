
from pydantic import BaseModel
from deta import Deta
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()
PROJECT_KEY = os.environ.get("PROJECT_KEY")

deta = Deta(PROJECT_KEY)
users = deta.Base("users")


class RssLink(BaseModel):
    ChatId: int
    Links: List[str]