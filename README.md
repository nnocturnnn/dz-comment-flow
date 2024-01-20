# SPA Commenting Application

## Slow-load
Time load page with sqlite 0.2s

Time load page with free postgress 16.1s

## Overview
This Single Page Application (SPA) allows users to leave comments, similar to a forum or a comment section on a blog post. The application is built using Django and a front-end framework of your choice (Vue, React, Angular). Users can post comments, reply to them, and sort comments based on various criteria.

## Features
- **User Comments**: Users can post comments and view them in real-time.
- **Nested Comments**: Support for nested comments or replies, allowing for detailed discussions.
- **Comment Sorting**: Ability to sort comments by User Name, E-mail, and Date Added in both ascending and descending order.
- **Pagination**: Comments are paginated to enhance performance and user experience.
- **File Attachments**: Users can attach images and text files to their comments.
- **CAPTCHA Integration**: A CAPTCHA system is integrated to prevent spam.
- **XSS and SQL Injection Protection**: The application is designed with security in mind, protecting against common web vulnerabilities.
- **Real-time Updates**: Utilizing WebSocket for real-time comment updates.

## Technology Stack
- **Back-end**: Django, Django ORM
- **Front-end**: HTML/CSS/React/Bootsrap
- **Database**: PostgreSQL/SQLite
- **Additional Tools**: Docker, Git, WebSocket
- **Security**: Implementations for protection against XSS and SQL Injection.
- **Cloud**: Artifact Registry, Cloud Bucket, Cloud Run

## TODO
- **Implement RabbitMQ**
- **Implement cache for last comments**
- **Add visual effects to Viewing files**


link https://my-django-app-isylms7vba-uc.a.run.app/

## Building and Running the Application with Docker

To build and run this application using Docker, follow these steps:

1. **Build the Docker Image**:
   Navigate to the root directory of your project where the Dockerfile is located and run:

    ```bash
    docker build -t spa-comment-app .
    ```

2. **Run the Docker Container**:
   To start the application in a container, run:

    ```bash
    docker run -d -p 8080:8080 spa-comment-app
    ```

3. **Access the Application**:
   The application will be accessible at `http://localhost:8080`.

Ensure you have Docker installed and running on your machine. This setup is ideal for development and testing. For production deployments, consider using a more robust server like Gunicorn or uWSGI and serve static files efficiently.

1. **Install Dependencies**:
   Ensure that you have Python installed on your machine. Then install the required Python packages, preferably in a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

2. **Database Setup**:
   Set up your database (SQLite, PostgreSQL, or MySQL) as specified in your Django settings. For SQLite, no additional setup is required.

3. **Run Migrations**:
   Apply database migrations to create the necessary database schema:

    ```bash
    python manage.py migrate
    ```

4. **Run the Application**:
   Start the Django development server:

    ```bash
    python manage.py runserver
    ```

5. **Access the Application**:
   The application will be accessible at `http://localhost:8000`.

Remember to adjust any specific settings or steps based on your project's configuration.