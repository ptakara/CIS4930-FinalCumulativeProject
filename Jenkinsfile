pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run') {
            steps {
                echo 'Running container...'
                sh 'docker run -d -p 8081:8080 flask-app'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing API...'
                sh 'curl http://localhost:8081/api/health'
            }
        }
    }
}
