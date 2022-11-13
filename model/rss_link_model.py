
from pydantic import BaseModel
from typing import List


class RssLink(BaseModel):
    ChatId: int
    Links: List[str]
