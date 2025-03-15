from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId

router = APIRouter(prefix='/tasks', tags=["Tasks"])

@router.post("")
async def addTask(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def getTasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {"data": tasks}
