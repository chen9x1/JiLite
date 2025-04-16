#!/bin/bash
echo "正在启动JiLite项目..."

# 检查虚拟环境是否存在
if [ ! -f "venv/Scripts/activate" ]; then
    echo "虚拟环境不存在，正在创建..."
    python -m venv venv
    echo "虚拟环境创建完成！"
fi

# 激活虚拟环境
echo "正在激活虚拟环境..."
source venv/Scripts/activate

# 安装依赖
# echo "正在安装项目依赖..."
# pip install -r requirements.txt

# 启动Flask应用
echo "正在启动Flask应用..."
python app.py

# 保持窗口打开
read -p "按任意键继续..." 