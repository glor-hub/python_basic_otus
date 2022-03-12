"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from http import HTTPStatus

from aiohttp import ClientSession, ClientResponse

from homework_04.models import (
    User,
    Post,
)

from typing import List


NUM_USERS = 10

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:  # : ClientResponse
        if response.status == HTTPStatus.OK:
            response_json = await response.json()
            return response_json


async def fetch_user_by_user_id(userId: int) -> User:
    async with ClientSession() as session:
        user_json = await fetch_json(session, USERS_DATA_URL + "/" + str(userId))
    id = user_json.get("id", 1)
    name = user_json.get("name", "")
    username = user_json.get("username", "")
    email = user_json.get("email", "")
    user = User(
        id=id,
        name=name,
        username=username,
        email=email
    )
    return user


async def fetch_posts_for_user(userId: int) -> List:
    posts_for_user = []
    async with ClientSession() as session:
        posts_json = list(await fetch_json(session, POSTS_DATA_URL + "?" + "userId=" + str(userId)))
    for post_json in posts_json:
        id = post_json.get("id", 0)
        user_id = post_json.get("userId", 0)
        title = post_json.get("title", "")
        body = post_json.get("body", "")
        post = Post(
            id=id,
            user_id=user_id,
            title=title,
            body=body
        )
        posts_for_user.append(post)
    return posts_for_user

async def fetch_users_data():
    return [await fetch_user_by_user_id(user_id)
             for user_id in range(1, NUM_USERS + 1)]


async def fetch_posts_data():
    return [await fetch_posts_for_user(user_id)
             for user_id in range(1, NUM_USERS + 1)]

async def get_data():
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )
    return users_data, posts_data

if __name__ == '__main__':
    asyncio.run(get_data())