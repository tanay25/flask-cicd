pipeline{

	agent any

	environment {
		IMAGE_NAME = "flask-cicd"
		DOCKER_USER = "tanay25"
	}

	stages {
		
		stage('clone repository') {

			steps {
				git branch:"main",
				url:"https://github.com/tanay25/flask-cicd.git"
			}
		}
		stage('Install Dependencies') {
			steps {
				sh '''
					python3 -m venv venv
					. venv/bin/activate
					pip install -r requirments.txt
	
				'''
			}

		}
		
		stage("Run Test") {
			steps {
			
				sh '''
					. venv/bin/activate
					pytest

				'''
			}
			
		}
		stage("Build Docker Image") {
			steps {
				sh '''
					docker build -t $DOCKER_USER/$IMAGE_NAME:latest .
				'''
			}
			
		}
		stage("Push Image to Dockerhub") {
			steps {
				withCredentials([usernamePassword(crendentialsId:'dockerhub-creds',usernameVariable:'USER',
				passwordVaraibale:'PASS')]){
				sh '''
					echo $PASS | docker login -u $USER --password-stdin
					docker push $DOCKER_USER/$IMAGE_NAME:latest
				'''
				}
			}
	
		}
		stage('Deploy Container') {
			steps {
				sh '''
					docker rm -f flask-app || true
					docker run -d -p 5000:5000 --name flask-app $DOCKER_USER/$IMAGE_NAME:latest

				'''
			}

		}
	}
	post{
		success {
			echo "CI/CD Pipeline Completed"
		}
		failure {
			echo "Pipeline failed "
		}
	}
}
