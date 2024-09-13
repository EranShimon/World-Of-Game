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
                    docker.build("scores-service")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.compose.up()
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def result = sh(script: 'python e2e.py', returnStatus: true)
                    if (result != 0) {
                        error "Tests failed"
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    docker.compose.down()
                    docker.image("scores-service").push("latest")
                }
            }
        }
    }
}