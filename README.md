# Flask Todo App

A simple web-based Todo application built using **Flask**. This app allows users to manage tasks (add, mark as done, delete) with a clean and straightforward interface.

---

## Features

- Add new tasks with descriptions.
- Mark tasks as "Done."
- Delete tasks from the list.
- User-friendly interface.
- Data persistence using a JSON file.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Data Storage**: JSON file

---

## Installation and Setup

Follow these steps to run the application locally:

### Prerequisites
- Python 3.x installed on your system.
- `pip` (Python package installer).

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Harish-2608/Todo_webapp.git
   cd Todo_webapp
   ```

2. **Install Dependencies**
   ```bash
   pip install flask
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Open in Browser**
   Open your browser and navigate to:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## File Structure

```
flask-todo-app/
│
├── app.py              # Main Flask application
├── operations.py       # Task management operations
├── json_util.py        # Utility functions for JSON file handling
├── task.json           # JSON file to store tasks
├── templates/          # HTML templates for Flask
   └── index.html      # Main page template
```

---

## Usage

1. **Add Task**: Enter a task description in the input field and click **"Add Task"**.
2. **Mark Done**: Click **"Mark Done"** to update the status of a task.
3. **Delete Task**: Click **"Delete"** to remove a task from the list.

---
