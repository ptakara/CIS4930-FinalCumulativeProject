pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
	
	stage('Verify Files') {
	    steps {
		sh 'ls -la'
		sh 'test -f Dockerfile'
		sh 'test -f requirements.txt'
		sh 'test -f app.py'
	    }
	}

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t quiz-app .'
            }
        }

        stage('Run') {
            steps {
                echo 'Running container...'
		sh 'docker rm -f quiz-app-test || true'
                sh 'docker run -d --name quiz-app-test -p 5000:5000 quiz-app'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing API...'
		sh 'sleep 3'
                sh 'curl http://localhost:5000/api/health'
            }
        }
    }

    post {
	always {
	    sh 'docker rm -f quiz-app-test || true'
	}
    }
}
