# Flask Quiz App

This project is a simple quiz application built with Flask.

## Tech Stack
- Flask
- Docker
- Jenkins
- GitHub

## Features
- Trivia quiz
- Score tracking (optional)
- CI/CD pipeline with Jenkins

## Jenkins Pipeline

This project uses Jenkins to automate the build and verification workflow.

Pipeline stages:
1. Checkout source code from GitHub
2. Verify required project files exist
3. Build the Docker image
4. Run the Flask app container
5. Verify the app using the `/api/health` endpoint
6. Clean up the test container
