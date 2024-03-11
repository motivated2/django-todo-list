## Task Manager Web Application

This is a simple web application for managing tasks and tags. It allows users to create, view, update, and delete tasks, as well as add, view, update, and delete tags associated with those tasks.

### Features

- **Task Management**: Users can create tasks with descriptions, deadlines, tags, and completion status. They can mark tasks as complete or incomplete, update task details, and delete tasks.
  
- **Tag Management**: Users can create tags to categorize tasks. They can view all existing tags, update tag names, and delete tags.
  
- **Home Page**: The home page displays a list of tasks sorted by completion status (not done to done) and creation date (newest to oldest). Each task shows its content, creation datetime, deadline datetime (if any), tags, and buttons for updating, deleting, and toggling completion status.
  
- **Tag List Page**: The tag list page displays all existing tags in a table format. Each tag has links for updating its name and deleting it. Users can also add new tags from this page.

### Installation and Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/task-manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd task-manager
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your web browser and go to `http://127.0.0.1:8000/` to access the home page.

### Usage

- **Home Page**: Here, you can view all tasks, mark them as complete or incomplete, update task details, delete tasks, and add new tasks.

- **Tag List Page**: This page lists all existing tags. You can update tag names, delete tags, and add new tags from here.

### Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request on GitHub.

### Acknowledgments

- This project was developed using Django, a high-level Python web framework.
- Special thanks to the contributors and maintainers of Django for creating such a powerful and easy-to-use framework.
 