# Flask Quiz App

This project is a simple riddle application built with Flask.

## Tech Stack
- Flask
- Docker
- Jenkins
- GitHub

## Features
- Riddle test
- Score tracking
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

## Setup Instructions
1. Clone the repository from GitHub
2. Start up a Jenkins container
   - Ensure Docker is installed via `docker --version`
   - `docker pull jenkins/jenkins:lts`
   - Create a volume via `docker volume create jenkins_home`
   - `docker run -d --name jenkins -u root -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts`
3. Make sure Jenkins has Docker installed via `docker exec -u root -it jenkins bash`, then within the shell `apt-get update` and `apt-get install -y docker.io`.
4. Configure Pipeline Job
   - Ensure pipeline definition set to `pipeline script from SCM`
   - Set to Git with repository link and branch properly specified
5. Build and run pipeline
