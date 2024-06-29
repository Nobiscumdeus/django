Below is a guide to launch the application

---

# Tasky

Tasky is a task management application built with Django. It allows users to manage tasks, view tasks on a dashboard, and organize them by status and priority.

## Getting Started

Follow these instructions to set up and run the Tasky app on your local machine using `pipenv`.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- pipenv (Python dependency manager)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/tasky.git
   cd benmore 
   ```

2. **Install `pipenv`:**

   ```bash
   pip install pipenv
   ```

3. **Install the dependencies:**

   ```bash
   pipenv install
   ```

4. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

5. **Apply the database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin user):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin account.

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/` to see the Tasky application.

### Features

- Task management: Create, update, and delete tasks.
- Dashboard: View tasks by status and priority.
- User authentication: Register and log in to manage tasks.

### Project Structure

- `benmore/`: Main project directory.
- `benmore/settings.py`: Project settings.
- `benmore/urls.py`: URL configurations.
- `benmore/views.py`: View functions.
- `benmore/templates/`: HTML templates.
- `benmore/static/`: Static files (CSS, JS, images).

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License

This project is licensed under the MIT License.

---
