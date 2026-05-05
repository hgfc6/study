# FastAPI 学习笔记

FastAPI 是一个用于构建 API 服务的现代 Python Web 框架。它基于 ASGI，常配合 `uvicorn` 运行。

## 安装

```shell
pip install -r requirements.txt
```

## 运行示例

```shell
uvicorn demo.app:app --reload
```

默认访问地址：

```text
http://127.0.0.1:8000
```

自动接口文档：

```text
http://127.0.0.1:8000/docs
```

## 核心知识点

1. 路由
   - `@app.get("/")`
   - `@app.post("/items")`
2. 路径参数
   - 例如 `/items/{item_id}`
3. 查询参数
   - 例如 `/items?keyword=python`
4. 请求体
   - 通常用 Pydantic 模型描述 JSON 结构。
5. 响应模型
   - 用 `response_model` 控制返回字段。
6. 异步视图
   - 使用 `async def` 定义异步接口。
7. 自动文档
   - FastAPI 会根据类型标注生成 OpenAPI 文档。

## 与 Flask 的主要区别

1. Flask 更轻量，核心概念简单，适合入门 Web。
2. FastAPI 更偏 API 服务，类型标注和自动文档是核心优势。
3. Flask 默认是 WSGI；FastAPI 是 ASGI，更适合异步场景。

## 当前示例

| 文件 | 说明 |
| --- | --- |
| [demo/app.py](./demo/app.py) | 路由、路径参数、查询参数、请求体、响应模型示例 |
