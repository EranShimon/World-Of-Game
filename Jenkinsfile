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
                    docker.build("${env.DOCKER_IMAGE}:${env.DOCKER_TAG}")
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('EranShimon/World-Of-Game').run('-p 8777:8777 -v $PWD/scores_file.txt:/scores_file.txt')
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
                    sh 'docker stop $(docker ps -q --filter ancestor=EranShimon/World-Of-Game)'
                    sh 'docker push EranShimon/World-Of-Game'
                }
            }
        }
    }
}
