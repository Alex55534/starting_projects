
print("Start to work about to_do")

def reading(filename):
    """
    Принимает имя файла, возвращает список задач.
    Если файл не существует, возвращает пустой список.

    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:       
            data = f.read()
        if not data:
            return []
        tasks = [line.strip() for line in data.split('\n') if line.strip()]
        return tasks       
    except FileNotFoundError:
        return []
def record(filename, tasks):
    """
    Принимает имя файла и список задач.
    Перезаписывает файл, сохраняя каждую задачу на новой строке.

    """    
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')

def delete_task(filename, tasks_text):
    tasks = reading(filename)
    if tasks_text in tasks:
        tasks.remove(tasks_text)
        record(filename, tasks)
        return True
    else:
        return False

filename = "text1.txt"
tasks = reading(filename)
while True:
    try:
        choice = int(input("Choice number of tasks write read delete file 1/2/3/4 "))
    except ValueError:
        continue
    if choice == 1:
        tasks = reading(filename)
        print(tasks)
        print("Your list")
    elif choice == 2:
        text = input("Write text for task write")
        if text:
            tasks.append(text)
            record(filename, tasks)
            print("Add task")
        else:
            print("Task don't add")
    elif choice == 3:
        text = input("Enter task for delete")
        if delete_task(filename, text):
            print("Task Delete")
        else:
            print("Task don't delete")
    elif choice == 4:
        print("Exit with programm")
        break
    else:
        print("It's not right move")
        
        





       