# 🕵️‍♂️List Controller

Project created with the objective of automate the process of control a list of prioritization cases, using this program my labor as Team Leader can focus on take strategic decisions instead of be watching a list all day.

---

# Introduction

---

The project using Python and Selenium creates and automated browser that takes screenshot of the webpage [https://m3s.materialise.net/CaseManagement/GridView](https://m3s.materialise.net/CaseManagement/GridView) every 5 minutes and struggle with the auto-logout tool of the web page to keep the log in. 

When the user run the script, the CMD is launched and it asks for a period of operation in minutes. After that, The script creates and stores every image in a folder in the same path where the script is located.

![Untitled](%F0%9F%95%B5%EF%B8%8F%E2%80%8D%E2%99%82%EF%B8%8FList%20Controller%20b0bce008c1374ac18155229bbc5d398f/Untitled.png)

# Objective

---

- Freeing up team leader time.
- Guarantee the most urgent cases are taken in the appropriate order by employees.
- Understand the behavior of the list.

# Technologies

---

- python==3.7.9.
- selenium==4.3.0.

**Note:** for more details open requirements.txt

# Setup

---

To run this project, download the code and in the main folder run.

```bash
python list_controller.py
```