\# 📋 Console To‑Do List



A minimal command‑line task manager written in Python.  

Tasks are stored in a plain text file (`text1.txt`).  

The interface is in \*\*Russian\*\*, but the code is easy to adapt.



\## ✨ What it can do



\- \*\*View tasks\*\* – read and display all saved tasks.

\- \*\*Add tasks\*\* – append a new task to the list.

\- \*\*Delete tasks\*\* – remove a specific task by its exact text.

\- \*\*Persistent storage\*\* – all changes are saved to `text1.txt` automatically.



\## 🚀 How to run



1\. Make sure you have Python \*\*3.6+\*\* installed.

2\. Clone the repository or download the script.

3\. (Optional) Create an empty `text1.txt` file, or the script will create it automatically.

4\. Run the program:



&#x20;  ```bash

&#x20;  python todo.py



🧠 How it works



The file text1.txt stores one task per line.



The program reads the entire file on start, keeps the list in memory, and writes back after each addition or deletion.



Simple functions:



reading(filename) – returns list of tasks.



record(filename, tasks) – overwrites the file with the current list.



delete\_task(filename, text) – removes a task by content.



📝 Example session



text



Start to work about to\_do



Choice number of tasks write read delete file 1/2/3/4 2



Write text for task write Buy milk



Add task



Choice number of tasks write read delete file 1/2/3/4 1



\['Buy milk']



Your list



Choice number of tasks write read delete file 1/2/3/4 4



Exit with programm

