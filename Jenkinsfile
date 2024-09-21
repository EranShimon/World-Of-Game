pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
    docker {
        image 'docker:latest'
            args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t "$JD_IMAGE" .'
            }
        }

        
        stage('Build') {
            steps {
                script {
                    docker.build('EranShimon/worldofgame')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('EranShimon/worldofgame').run('-p 8777:8777 -v $PWD/Scores.txt:/Scores.txt')
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
                    sh 'docker stop $(docker ps -q --filter ancestor=EranShimon/worldofgame)'
                    sh 'docker push EranShimon/worldofgame'
                }
            }
        }
    }
}
