"""
命令行待办事项（Todo List）
练习内容：列表操作、文件读写、字典、循环
数据保存在同目录的 todos.json 中
"""

import json
import os

DATA_FILE = "todos.json"

def load_todos():
    """从文件加载待办事项"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    """保存待办事项到文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def show_todos(todos):
    """显示所有待办事项"""
    if not todos:
        print("暂无待办事项")
        return
    
    print("\n=== 待办事项列表 ===")
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo["done"] else "⬜"
        print(f"{i}. {status} {todo['title']}")
    print()

def add_todo(todos):
    """添加待办事项"""
    title = input("请输入待办事项：").strip()
    if title:
        todos.append({"title": title, "done": False})
        print("添加成功！")
    else:
        print("内容不能为空")

def complete_todo(todos):
    """标记完成"""
    show_todos(todos)
    try:
        idx = int(input("请输入要完成的序号：")) - 1
        if 0 <= idx < len(todos):
            todos[idx]["done"] = True
            print(f"已完成：{todos[idx]['title']}")
        else:
            print("无效的序号")
    except ValueError:
        print("请输入数字")

def delete_todo(todos):
    """删除待办事项"""
    show_todos(todos)
    try:
        idx = int(input("请输入要删除的序号：")) - 1
        if 0 <= idx < len(todos):
            removed = todos.pop(idx)
            print(f"已删除：{removed['title']}")
        else:
            print("无效的序号")
    except ValueError:
        print("请输入数字")

def main():
    todos = load_todos()
    
    while True:
        print("\n=== 待办事项管理 ===")
        print("1. 查看列表")
        print("2. 添加事项")
        print("3. 完成事项")
        print("4. 删除事项")
        print("0. 退出")
        
        choice = input("选择操作：").strip()
        
        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
            save_todos(todos)
        elif choice == "3":
            complete_todo(todos)
            save_todos(todos)
        elif choice == "4":
            delete_todo(todos)
            save_todos(todos)
        elif choice == "0":
            print("再见！")
            break
        else:
            print("无效的选择")

if __name__ == "__main__":
    main()
