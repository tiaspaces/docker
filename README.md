# docker
Developing Hands-On Skills on Docker



# Docker Hands-On Walkthrough

## Introduction

This guide will walk you through the basics of Docker, including creating a Dockerfile, building an image, running a container, debugging, and using Docker Compose. By the end of this tutorial, you will have a simple Python web application running in a Docker container.

---

## What is Docker?

Docker is a platform for developing, shipping, and running applications in containers. Containers allow you to package an application with all its dependencies and run it consistently across different environments.

---

## Step 1: Setup

### Browse to labs.tiaspaces.com


2. **Launch TiaSpaces**:
   - click on terminal and run the following:
     ```bash
     docker --version
     ```
   - You should see the Docker version information.


## Step 2: Create a Dockerfile

1. **Create a New Directory**:
   - Open a terminal and create a new directory for your project:
     ```bash
     mkdir my-docker-project
     cd my-docker-project
     ```

2. **Open TiaSpaces**:
   - Open the newly created directory in TiaSpaces.

3. **Create a Dockerfile**:
   - In TiaSpaces, click on `File > New File`, name it `Dockerfile`, and save it in the project directory.
   - Add the following content to the `Dockerfile`:
     ```Dockerfile
     # Use an official Python runtime as a parent image
     FROM python:3.8-slim

     # Set the working directory in the container
     WORKDIR /app

     # Copy the current directory contents into the container at /app
     COPY . /app

     # Install any needed packages specified in requirements.txt
     RUN pip install --no-cache-dir -r requirements.txt

     # Make port 80 available to the world outside this container
     EXPOSE 80

     # Define environment variable
     ENV NAME World

     # Run app.py when the container launches
     CMD ["python", "app.py"]
     ```

   ![Dockerfile in TiaSpaces](screenshots/dockerfile.png)

4. **Create `requirements.txt`**:
   - In TiaSpaces, click on `File > New File`, name it `requirements.txt`, and save it in the project directory.
   - Add the following content to `requirements.txt`:
     ```text
     Flask
     ```

   ![requirements.txt in TiaSpaces](screenshots/requirements.png)

5. **Create `app.py`**:
   - In TiaSpaces, click on `File > New File`, name it `app.py`, and save it in the project directory.
   - Add the following content to `app.py`:
     ```python
     from flask import Flask
     app = Flask(__name__)

     @app.route('/')
     def hello():
         return "Hello, World!"

     if __name__ == "__main__":
         app.run(host="0.0.0.0", port=80)
     ```

   ![app.py in TiaSpaces](screenshots/app.png)

---

## Step 3: Build an Image

1. **Build the Docker Image**:
   - Open a terminal in TiaSpaces by clicking `Terminal > New Terminal`.
   - Run the following command to build the Docker image:
     ```bash
     docker build -t my-python-app .
     ```
   - You should see the build process in the terminal.

   ![Building Docker Image](screenshots/build.png)

---

## Step 4: Run a Container

1. **Run the Docker Container**:
   - In the terminal, run the following command to start the container:
     ```bash
     docker run -p 4000:80 my-python-app
     ```
   - The container will start, and you should see log output in the terminal.

   ![Running Docker Container](screenshots/run.png)

2. **Open in Browser**:
   - Open your web browser and go to `http://localhost:4000`.
   - You should see the message "Hello, World!".

   ![Hello World in Browser](screenshots/hello.png)

---

## Step 5: Debugging

1. **Check Container Logs**:
   - In the terminal, run:
     ```bash
     docker logs <container_id>
     ```
   - Replace `<container_id>` with the actual container ID, which you can find by running `docker ps`.

   ![Docker Logs](screenshots/logs.png)

2. **Access Container Shell**:
   - To access the shell of the running container, run:
     ```bash
     docker exec -it <container_id> /bin/sh
     ```
   - Replace `<container_id>` with the actual container ID.

   ![Accessing Container Shell](screenshots/shell.png)

---

## Step 6: Docker Compose

1. **Create `docker-compose.yml`**:
   - In TiaSpaces, click on `File > New File`, name it `docker-compose.yml`, and save it in the project directory.
   - Add the following content to `docker-compose.yml`:
     ```yaml
     version: '3'
     services:
       web:
         image: my-python-app
         build: .
         ports:
           - "4000:80"
     ```

   ![docker-compose.yml in TiaSpaces](screenshots/compose.png)

2. **Build and Run with Docker Compose**:
   - In the terminal, run:
     ```bash
     docker-compose up
     ```
   - Docker Compose will build and start the container, and you should see log output in the terminal.

   ![Docker Compose Up](screenshots/compose-up.png)

3. **Open in Browser**:
   - Open your web browser and go to `http://localhost:4000`.
   - You should see the message "Hello, World!" again.

   ![Hello World in Browser](screenshots/hello.png)

---

## Conclusion

You have successfully created a Dockerfile, built a Docker image, run a Docker container, debugged the container, and used Docker Compose to manage your application. Your Python web application is now running inside a Docker container, and you can share your project with others knowing it will work the same way on their systems.

