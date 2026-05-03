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
                sh 'docker build -t riddle-app .'
            }
        }

        stage('Run') {
            steps {
                echo 'Running container...'
		sh 'docker rm -f riddle-app-test || true'
                sh 'docker run -d --name riddle-app-test -p 5000:5000 riddle-app'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing API...'
		sh 'sleep 5'
                sh """ docker exec riddle-app-test python3 -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000/api/health/').read().decode())" """
            }
        }
    }

    post {
	always {
	    sh 'docker logs riddle-app-test || true'
	    sh 'docker rm -f riddle-app-test || true'
	}
    }
}
