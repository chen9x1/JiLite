@echo off
echo 正在启动JiLite项目...

:: 检查虚拟环境是否存在
if not exist venv\Scripts\activate.bat (
    echo 虚拟环境不存在，正在创建...
    python -m venv venv
    echo 虚拟环境创建完成！
)

:: 激活虚拟环境
echo 正在激活虚拟环境...
call venv\Scripts\activate.bat

:: 安装依赖
:: echo 正在安装项目依赖...
:: pip install -r requirements.txt

:: 启动Flask应用
echo 正在启动Flask应用...
python app.py

:: 保持窗口打开
pause 