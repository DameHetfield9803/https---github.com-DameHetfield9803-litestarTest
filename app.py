from litestar import Litestar, get

@get("/")
async def hello_world() -> str:
    return "Hello world"

@get("/welcome")
async def welcome() -> str:
    return '''Welcome to my litestar app'''

@get("/about")
async def about() -> str:
    return '''About us\nYou make the product, we solve the problems.'''

app = Litestar([hello_world, welcome, about])