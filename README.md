# Google Authentication 🔑

This project is a Flask-based web application that utilizes Google OAuth 2.0 for authentication. It demonstrates how to authenticate users via Google, displaying a simple web interface for login and showing the access token upon successful authentication.

## Features 🚀

- **Google OAuth 2.0 Integration**: Securely authenticate users with Google.
- **Flask Web Application**: A lightweight web server handling OAuth callbacks and serving HTML content.
- **Docker Support**: Containerize the application for easy deployment and scaling.

## Prerequisites 📋

Before you begin, ensure you have met the following requirements:
- Python 3.9 or higher
- Docker (for containerization)

## Installation 🛠️

1. **Clone the repository**

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
   ```

2. **Set up a virtual environment (Optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application 🏃

### Locally (without Docker)

1. **Start the Flask application**

   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:5000`.

### Using Docker 🐳

1. **Build the Docker image**

   ```bash
   docker build -t google-auth-app .
   ```

2. **Run the Docker container**

   ```bash
   docker run -p 8080:8080 google-auth-app
   ```

   The application will be available at `http://localhost:8080`.

## Usage 🧑‍💻

- Navigate to the application URL.
- Click on the "Login with Google" button.
- You will be redirected to Google's OAuth 2.0 login page.
- After logging in, you will be redirected back to the application, where your access token will be displayed.
