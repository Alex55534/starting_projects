print("Text of analyzer")

def read_file(filename):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = f.read()
        if not data:
            return []
        else:   
            tasks =[line.strip() for line in data.split('\n') if line.strip()]
            return tasks
    except FileNotFoundError:
        return []

def record(filename, tasks):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in tasks:
            f.write(i + '\n')
            
def analyz_char(filename):
    letter_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for word in f:
            for char in word:
                if char.isalpha():
                    letter_count +=1
        return letter_count

def analyz_word(filename):
    counter = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words_in_line = line.split()
            counter = counter + len(words_in_line)
        return counter

                
filename = 'analyz.txt'
tasks = read_file(filename)
print("Menu for selection 1/2/3/4")
while True:
    try:
        choice = int(input("Enter number 1-reading text, 2-record text 3-counting letters, 4-countig word, 5-exit"))
    except ValueError:
        print("Enter only numbers")
        continue
    if choice == 1:
        tasks = read_file(filename)
        print("\n".join(tasks))
    elif choice == 2:
        text = input("Enter your text")
        if text:
            tasks.append(text)
            record(filename, tasks)
    elif choice == 3:
        anal = analyz_char(filename)
        print(anal)
    elif choice == 4:
        total = analyz_word(filename)
        print(total)
    elif choice == 5:
        break

