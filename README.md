# JiLite项目文档：Autosys Job 查询 API

## 一、项目概述

JiLite 是一个轻量级的 Autosys JIL 文件解析和RESTful API服务。

### 1. 项目简介

项目名称： JiLite

本项目基于 Flask 2.2.5 框架开发，旨在为前端提供 RESTful 风格的 API 接口，实现对 Autosys Job 的查询功能。项目采用蓝图组织结构和分层设计，以确保具备良好的可扩展性和高维护性。系统不涉及用户登录鉴权和多 API 版本管理。

### 2. 技术栈

框架：Flask 2.2.5
数据交互：使用 Python 相关库与 Autosys 系统进行交互，获取 Job 信息

### 3. 设计原则

- 模块化：通过蓝图将不同功能模块分离，便于管理和扩展。
- 分层架构：分为接口层、服务层和数据访问层，职责明确，提高代码的可维护性。
- 单一职责：每个模块和函数只负责单一功能。

## 二、项目结构

```plaintext
JiLite/
├── app/
│   ├── __init__.py           # 应用初始化
│   ├── api/
│   │   ├── __init__.py       # 蓝图注册
│   │   ├── autosys/
│   │   │   ├── __init__.py   # Autosys 蓝图
│   │   │   ├── routes.py     # Autosys 路由
│   │   │   ├── views.py      # Autosys 视图逻辑（服务层）
│   │   │   ├── models.py     # Autosys 数据模型（数据访问层）
│   │   │   ├── schemas.py    # Autosys 数据序列化器
│   ├── utils/                # 工具函数
│   ├── static/               # 静态资源（可选）
│   └── templates/            # 模板目录（可选）
├── instance/
│   └── config.py             # 配置文件
├── .env.example              # 环境变量示例
├── requirements.txt          # 依赖清单
├── README.md                 # 项目文档
└── app.py                    # 应用入口
```

## 三、API 接口规范

### 1. 通用规范

请求格式：JSON 格式（Content-Type: application/json）
响应格式：
```json
{
    "data": {},
    "message": "",
    "code": 0
}
```

### 2. 接口（Autosys Job 查询）

#### 2.1 查询所有 Autosys Jobs

端点：GET /api/autosys/jobs
功能：获取所有 Autosys Jobs 的信息
响应示例（成功）：
```json
{
    "data": [
        {
            "job_name": "job1",
            "status": "running",
            "last_run_time": "2025-04-09 10:00:00"
        },
        {
            "job_name": "job2",
            "status": "completed",
            "last_run_time": "2025-04-08 14:30:00"
        }
    ],
    "message": "获取所有作业成功",
    "code": 0
}
```
#### 2.2 根据 Job 名称查询单个 Autosys Job

端点：GET /api/autosys/jobs/<job_name>
功能：根据 Job 名称获取单个 Autosys Job 的详细信息
响应示例（成功）：

```json
{
    "data": {
        "job_name": "job1",
        "status": "running",
        "last_run_time": "2025-04-09 10:00:00"
    },
    "message": "获取作业 'job1' 成功",
    "code": 0
}
```

#### 2.3 错误处理示例

端点错误：404 Not Found

```json
{
    "data": null,
    "message": "未找到作业: 'nonexistent'",
    "code": -1
}
```

## 四、可扩展性与维护性设计

### 1. 模块化扩展

新增功能模块时，可创建新的蓝图目录，包含独立的 routes.py、views.py、models.py 和 schemas.py 文件。
若需与其他系统集成，可在相应的蓝图中添加新的接口。

### 2. 环境配置

通过 config.py 管理不同环境（开发、测试、生产）的配置。
敏感信息（如数据库连接信息）可通过 .env 文件管理。

### 3. 分层架构说明

接口层（API）：负责处理路由分发、请求解析和响应封装，调用服务层逻辑。
服务层（Service）：包含业务逻辑，如数据校验、数据处理等，调用数据访问层获取数据。
数据访问层（DAO）：负责与 Autosys 系统或数据库进行交互，提供数据查询、存储等操作。
工具函数（Utils）：提供通用的工具函数，如日志记录、异常处理等。

### 4. 代码规范

使用类型注解提高代码可读性。
遵循 PEP8 编码规范，采用蛇形命名法。
关键逻辑添加注释，重要接口提供文档字符串。