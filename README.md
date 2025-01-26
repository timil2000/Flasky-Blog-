# Flasky-Blog-
A dynamic blog application built with Flask, featuring secure user authentication, post management, and a mobile-friendly responsive design. Perfect for learning full-stack web development and modern web design principles

## Features
- **User Authentication**: Secure user registration, login, and logout.
- **Password Reset**: Request and reset passwords via email.
- **Post Management**: Create, read, update, and delete posts.
- **User Profiles**: Manage account information and profile pictures.
- **Pagination**: View posts with pagination for better navigation.
- **Responsive Design**: Mobile-friendly and responsive layout using Bootstrap.

## Project Structure
```
E:/flaskblog
│   flaskblog.iml
│   requirements.txt
│   run.py
├───.idea
├───flaskBlog
│   ├───errors
│   ├───main
│   ├───posts
│   ├───static
│   ├───templates
│   ├───users
│   └───__pycache__
├───instance
└───__pycache__
```

### Key Directories
- `flaskBlog`: Main application folder containing configurations, models, and blueprints for errors, posts, users, and main routes.
- `static`: Contains static files like CSS, images, and JS.
- `templates`: HTML templates for rendering web pages, including reusable layouts and individual views.
- `instance`: Database files (`flaskblog.db`, `site.db`).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flaskblog.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flaskblog
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set environment variables for Flask:
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```
7. Initialize the database:
   ```bash
   flask db upgrade
   ```
8. Run the application:
   ```bash
   flask run
   ```

## Usage
1. Access the application in your web browser at `http://127.0.0.1:5000/`.
2. Register as a new user or log in with an existing account.
3. Create, edit, or delete posts, and manage your profile settings.

## Screenshots
*Include screenshots of the application, such as the home page, user profile, and post creation view.*

## Technologies Used
- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, CSS, Bootstrap 4
- **Database**: SQLite
- **Others**: Flask-WTF, Flask-Mail

## Contributing
Contributions are welcome! Feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
