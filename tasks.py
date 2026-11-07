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
def add_task(tasks, title):
    title = title.strip()

    if not title:
        return "empty"

    for existing_title, completed in tasks:
        if title == existing_title:
            return "duplicate"

    tasks.append((title, False))
    return "success"

        
