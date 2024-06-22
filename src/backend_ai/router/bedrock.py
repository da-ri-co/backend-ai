from typing import List
from fastapi import APIRouter, Depends, HTTPException, FastAPI, Response
from fastapi.responses import Response

import asyncio

import requests
import os

from pydantic import BaseModel


class timeline(BaseModel):
    start: int
    end: int
    speaker: str
    content: str


from llm.chat import chat

bedrock_router = APIRouter()


@bedrock_router.post("/summerize/")
async def output(
    timelines: List[timeline],
):
    print(timelines)
    p = ""
    for i in timelines:
        print(i.content)
        p += "" + str(i.start) + " : " + str(i.speaker) + " : " + str(i.content) + "\n"
    payload = p
    print(payload)
    res = chat(payload)

    return Response(
        content=await res,
        status_code=200,
        headers={"Content-Type": "text/plain", "Cache-Control": "no-cache"},
    )


@bedrock_router.get("/check_health")
async def hello():
    return {"message": "ok"}
