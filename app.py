from litestar import Litestar, get, post

TODO_LIST: list[dict[str, str | bool]] = [
    {"title": "Start writing TODO list", "done": True},
    {"title": "???", "done": False},
    {"title": "Profit", "done": False},
]


@get("/welcome")
async def welcome() -> str:
    return '''Welcome to my litestar app'''

@get("/about")
async def about() -> str:
    return '''About us\nYou make the product, we solve the problems.'''

@get("/")
async def get_list() -> list[dict[str, str | bool]]:
    return TODO_LIST

app = Litestar([welcome, about, get_list])