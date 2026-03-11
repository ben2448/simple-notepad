# 简易记事本
import os

def show_menu():
    print("\n===== 简易记事本 =====")
    print("1. 查看笔记")
    print("2. 添加笔记")
    print("3. 退出")
    return input("请选择(1/2/3): ")

def read_note():
    print("\n===== 你的笔记 =====")
    if os.path.exists("note.txt"):
        with open("note.txt", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("暂无笔记")

def add_note():
    content = input("\n输入要添加的内容: ")
    with open("note.txt", "a", encoding="utf-8") as f:
        f.write(content + "\n")
    print("添加成功！")

while True:
    choice = show_menu()
    if choice == "1":
        read_note()
    elif choice == "2":
        add_note()
    elif choice == "3":
        print("再见！")
        break
    else:
        print("输入错误，请重新选择")
