def show_tasks(tasks):
    print("\n===== 当前任务 =====")
    for index, (title, completed) in enumerate(tasks, start=1):
        mark = "✓" if completed else " "
        print(f"{index}. [{mark}] {title}")

    completed_count = sum(completed for _, completed in tasks)
    print(
        f"\n共 {len(tasks)} 个任务，已完成 {completed_count} 个，"
        f"未完成 {len(tasks) - completed_count} 个。"
    )


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
            if title:
                tasks.append((title, False))
                print("已添加任务。")
            else:
                print("任务名称不能为空。")
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
                title, _ = tasks[index]
                tasks[index] = (title, True)
                print("已标记任务完成。")
            else:
                tasks.pop(index)
                print("已删除任务。")
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

