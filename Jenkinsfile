pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('your-dockerhub-username/your-image-name')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('your-dockerhub-username/your-image-name').run('-p 8777:8777 -v $PWD/Scores.txt:/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('Tests failed')
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop $(docker ps -q --filter ancestor=your-dockerhub-username/your-image-name)'
                    sh 'docker push your-dockerhub-username/your-image-name'
                }
            }
        }
    }
}
