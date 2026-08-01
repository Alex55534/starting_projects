from datetime import datetime

def enter_text(text):
    return input(text)

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
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')

def search_notes(keyword, lines):
    enter_text("Searching word")
    keyword_lower = keyword.lower()
    found = []
    for line in lines:
        if keyword_lower in line.lower():
            found.append(line.strip())
    return found


text = enter_text("Any text")
current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
result = f"[{text} + [{current_date}]]"
file = "text for diary"
if enter_text:
    tasks = reading(file)
    tasks.append(result)
    record(file, tasks)

while True:
    enter = input("Enter  few comands, show, exit")
    if enter == "show":
        with open(file, 'r', encoding='utf-8') as f:
            content = (f.read())
            print(content) 
            all_lines = f.readlines()
            results = search_notes(enter_text, all_lines)
            if content == None:
                print("No records found")
    elif enter =="exit":
        break
    else:
        print("Unknown command entered ")




    