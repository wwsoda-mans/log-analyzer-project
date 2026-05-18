# Log Analyzer Project

## Overview

Log Analyzer Project is a Python-based application developed for reading, analyzing, and processing system log files.

The main goal of this project is to simplify log monitoring and help users quickly identify important system events such as errors, warnings, and informational messages.

The system automatically reads log files, validates the data, filters incorrect entries, and generates useful statistics.

This project was developed as a group project using GitHub, Git branches, and PyCharm.

---

# Features

## Main Functionalities

- Read log files from .txt files
- Parse log entries line by line
- Validate incorrect or broken logs
- Separate logs by level
- Display processed information
- Count log statistics
- Handle invalid input safely
- Modular program structure

---

# Log Levels Supported

The system supports the following log levels:

- INFO
- WARNING
- ERROR

Example:

2026-05-18 | INFO | User logged in
2026-05-18 | WARNING | CPU usage is high
2026-05-18 | ERROR | Database connection failed

---

# Technologies Used

## Programming Language

- Python 3

## Development Environment

- PyCharm
- Git
- GitHub

---

# Python Concepts Used

This project includes many important Python programming concepts.

## 1. File Handling

Used for opening and reading log files.

Functions used:

open()
read()
write()

Purpose:
- reading logs
- saving data
- processing text files

---

## 2. Object-Oriented Programming (OOP)

Classes and objects were used to represent logs and organize the system structure.

Concepts used:
- Classes
- Objects
- Constructors
- Attributes

Example:

class Log:

---

## 3. Functions

Functions were created to divide the program into smaller reusable parts.

Example:

def parse_logs():

Functions help:
- improve readability
- reduce repeated code
- simplify debugging

---

## 4. Iteration

Loops were used for processing logs one by one.

Concepts used:
- for loops
- while loops

Example:

for line in file:

---

## 5. Conditional Statements

Conditions were used for checking log levels and validating data.

Example:

if level == "ERROR":

Used for:
- filtering logs
- validating input
- checking conditions

---

## 6. Lists and Data Storage

Lists were used to store log objects and processed data.

Example:

logs = []

---

## 7. String Manipulation

Used for splitting and cleaning log data.

Functions used:

split()
strip()

Purpose:
- remove spaces
- separate data
- clean text

---

## 8. Validation

Validation logic was implemented to detect:
- empty lines
- incorrect formats
- broken logs
- missing values

---

# Project Structure

project/
│
├── main.py
├── parser.py
├── validator.py
├── file_handler.py
├── models.py
├── utils.py
├── logs.txt
└── README.md

---

# How The Program Works

## Step-by-Step Workflow

1. User runs the program
2. System opens the log file
3. Logs are read line by line
4. Data is validated
5. Incorrect logs are skipped
6. Valid logs are processed
7. Statistics are generated
8. Results are displayed

---

# Example Workflow

Input:

2026-05-18 | ERROR | Database failed
2026-05-18 | INFO | User logged in

Output:

Total logs: 2
Errors: 1
Info: 1

---

# Error Handling

The system safely handles:
- missing files
- empty files
- invalid log formats
- broken entries

Example:

try:

---

# Team Collaboration

The project was developed collaboratively using GitHub branches.

Each team member worked independently on their own branch.

Workflow:
1. Create branch
2. Write code
3. Commit changes
4. Push branch to GitHub
5. Merge into main branch

Git commands used:

git branch
git checkout
git add .
git commit -m "message"
git push

---

# Why This Project Is Useful

This project helps:
- understand file processing
- practice Python programming
- learn teamwork with GitHub
- improve debugging skills
- understand modular programming

---

# Future Improvements

Possible future updates:
- graphical user interface (GUI)
- real-time log monitoring
- advanced filtering
- database support
- export reports
- search functionality

---

# Conclusion
Log Analyzer Project demonstrates practical usage of Python programming concepts, teamwork using GitHub, and modular software development.

The project provides a simple and effective solution for analyzing and processing system logs.

---

# Authors

SE-2524 Students  
Astana IT University

- Team Member 1 Kadashov Alikhan
- Team Member 2 Kaiyr Abilmansur
- Team Member 3 Bogdat Batyrkhan
- Team Member 4 Konakbay Yerassyl
