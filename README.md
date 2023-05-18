# Django Project Setup Guide for Beginners

This guide provides step-by-step instructions for beginners on how to set up and run a Django project. Django is a powerful web framework written in Python that simplifies the development of web applications. By following these instructions, you will learn how to install Python, set up your project directory, and run your Django project on your local machine. Let's get started!

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (version 3.6 or higher)
- pip (Python package manager)

## Installing Python

### Windows

1. Visit the [Python Downloads](https://www.python.org/downloads/windows/) page.
2. Download the latest version of Python for Windows by clicking on the "Download Python x.x.x" button.
3. Run the installer executable.
4. Select the "Add Python to PATH" option during the installation process.
5. Follow the prompts and complete the installation.

### macOS

1. Visit the [Python Downloads](https://www.python.org/downloads/mac-osx/) page.
2. Download the latest version of Python for macOS by clicking on the "Download Python x.x.x" button.
3. Run the installer package.
4. Follow the prompts and complete the installation.

### Linux

The process of installing Python on Linux may vary depending on the distribution you are using. Here's a general method using the command line:

1. Open a terminal.
2. Update the package list by running the following command:

   ```shell
   sudo apt update
   ```

3. Install Python by running the following command:

   ```shell
   sudo apt install python3
   ```

4. Verify the installation by checking the installed Python version:

   ```shell
   python3 --version
   ```

   The command should display the Python version installed.

## Setting up the Project Directory

1. Clone the project repository from GitHub or obtain the project files in any other way.
2. Open a terminal or command prompt and navigate to the project directory.

## Installation

1. Create a virtual environment for your project. Run the following command:

   ```shell
   python -m venv myenv
   ```

2. Activate the virtual environment. Use the appropriate command for your operating system:

   - **Windows**:

     ```shell
     myenv\Scripts\activate
     ```

   - **macOS/Linux**:

     ```shell
     source myenv/bin/activate
     ```

3. Install the required dependencies using `pip`. Run the following command:

   ```shell
   pip install -r requirements.txt
   ```

   This command will install all the necessary packages specified in the `requirements.txt` file.

4. Create the database tables by running the migrations. Execute the following command:

   ```shell
   python manage.py migrate
   ```

5. (Optional) If the project uses static files, collect them using the following command:

   ```shell
   python manage.py collectstatic
   ```

   This command will gather all the static files into a single directory for easier deployment.

6. (Optional) Load any initial data fixtures into the database. If the project provides fixtures, run the following command:

   ```shell
   python manage.py loaddata fixtures/*.json
   ```

   This will populate the database with initial data.

## Running the Project

After completing the installation steps, you are ready to run the Django project:

1. Start the development server with the following command:

   ```shell
   python manage.py runserver
   ```

2. Open a web browser and navigate to `http://localhost:8000/`. You should see the default Django landing page.

   Congratulations

! Your Django project is now up and running locally.

## Next Steps

Now that you have successfully set up and run your Django project, you can start exploring and customizing it. Here are a few additional resources to help you learn more about Django:

- [Django Official Documentation](https://docs.djangoproject.com/): The official documentation is a comprehensive guide to all aspects of Django.
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/): The official Django tutorial is an excellent resource for learning the basics of Django.
- [Django Girls Tutorial](https://tutorial.djangogirls.org/): This tutorial provides a beginner-friendly introduction to Django.

Enjoy developing your Django project! If you encounter any issues or have further questions, don't hesitate to seek help from the Django community or consult the documentation.

# Admin Panel

Login: `root`

Password: `root`

[Panel](http://127.0.0.1:8000/admin)