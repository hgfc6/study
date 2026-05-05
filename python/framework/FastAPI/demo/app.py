"""
FastAPI 最小 API 示例。

运行方式：
    uvicorn demo.app:app --reload

访问文档：
    http://127.0.0.1:8000/docs
"""

from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field


app = FastAPI(
    title="Study FastAPI Demo",
    description="用于学习 FastAPI 路由、参数、请求体和响应模型的最小示例。",
    version="0.1.0",
)


class ItemCreate(BaseModel):
    """
    创建商品时的请求体模型。

    BaseModel 来自 Pydantic，负责把 JSON 转换成 Python 对象，并执行基础校验。
    """

    name: str = Field(min_length=1, max_length=50, description="商品名称")
    price: float = Field(gt=0, description="商品价格，必须大于 0")
    tags: list[str] = Field(default_factory=list, description="商品标签")


class Item(ItemCreate):
    """
    商品响应模型。

    继承 ItemCreate 可以复用字段，再增加服务端生成的 id。
    """

    id: int


# 使用内存字典模拟数据库，重启服务后数据会丢失。
# 学习路由和参数时先用这种方式，能避免数据库配置干扰。
ITEMS: dict[int, Item] = {
    1: Item(id=1, name="Python Book", price=99.0, tags=["book", "python"]),
    2: Item(id=2, name="Keyboard", price=299.0, tags=["hardware"]),
}


@app.get("/")
async def read_root() -> dict[str, str]:
    """根路由通常用于健康检查或欢迎信息。"""

    return {"message": "Hello FastAPI"}


@app.get("/items", response_model=list[Item])
async def list_items(
    keyword: Annotated[
        str | None,
        Query(description="按商品名称关键字过滤，不传则返回全部"),
    ] = None,
) -> list[Item]:
    """
    查询商品列表。

    keyword 是查询参数，对应 URL 形如 /items?keyword=python。
    """

    items = list(ITEMS.values())

    if keyword is None:
        return items

    keyword_lower = keyword.lower()

    return [
        item
        for item in items
        if keyword_lower in item.name.lower()
    ]


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    """
    根据 ID 查询商品。

    item_id 是路径参数，对应 URL 形如 /items/1。
    """

    item = ITEMS.get(item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@app.post("/items", response_model=Item, status_code=201)
async def create_item(payload: ItemCreate) -> Item:
    """
    创建商品。

    payload 来自请求体 JSON，FastAPI 会自动解析并校验。
    """

    next_id = max(ITEMS) + 1 if ITEMS else 1
    item = Item(id=next_id, **payload.model_dump())
    ITEMS[next_id] = item

    return item
