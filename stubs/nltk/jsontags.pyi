import json

from _typeshed import Incomplete

__all__ = [
    "register_tag",
    "json_tags",
    "JSONTaggedEncoder",
    "JSONTaggedDecoder",
]

json_tags: Incomplete

def register_tag(cls: Incomplete) -> Incomplete: ...

class JSONTaggedEncoder(json.JSONEncoder):
    def default(self, obj: Incomplete) -> Incomplete: ...

class JSONTaggedDecoder(json.JSONDecoder):
    def decode(self, s: Incomplete) -> Incomplete: ...
    @classmethod
    def decode_obj(cls: Incomplete, obj: Incomplete) -> Incomplete: ...
