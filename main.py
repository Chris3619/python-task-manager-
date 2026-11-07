from tasks import show_tasks
from tasks import add_task
def read_task_index(tasks):
    try:
        index = int(input("请输入任务编号: "))
    except ValueError:
        return None
    if 1 <= index <= len(tasks):
        return index - 1
    return None
def main():
    tasks = [("学习 Python", True), ("学习 Git", True), ("学习 Linux", False)]
    menu = """===== TASK MANAGER =====
1. 添加任务
2. 查看所有任务
3. 标记任务完成
4. 删除任务
5. 退出程序
"""
    while True:
        print(menu)
        choice = input("请选择操作 (1-5): ").strip()

        if choice == "1":
            title = input("请输入任务名称: ").strip()
            result = add_task(tasks,title)
            if result == "success" :
                print("添加成功")
            elif result == "empty":
                print("添加失败，该任务不能为空")
            else:
                print("添加失败，任务已存在")
        elif choice == "2":
            show_tasks(tasks)
        elif choice in ("3", "4"):
            if not tasks:
                print("当前没有任务。")
                continue
            show_tasks(tasks)
            index = read_task_index(tasks)
            if index is None:
                print("无效的任务编号。")
            elif choice == "3":
                title, state = tasks[index]
                if state == True:
                    print("该任务已经完成，无需标记")
                else:
                    tasks[index] = (title, True)
                    print("已标记任务完成。")
            else:
                title,_=tasks[index]
                print(f"即将删除任务名称为：{title}")
                ans = input("请确认是否删除（输入y删除，n取消删除）：")
                if ans == "y":
                    tasks.pop(index)
                    print("已删除任务。")
                elif ans == "n":
                    print("取消删除")
                else:
                    print("请输入y或者n")
                    continue
        elif choice == "5":
            return
        else:
            print("无效选项，请输入 1 到 5。")
        print()


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print()



