pipeline {
    agent any

    environment {
        IMAGE_NAME = "scores-service"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
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
            parallel {
                stage('Unit Tests') {
                    steps {
                        script {
                            def result = sh(script: 'python unit_tests.py', returnStatus: true)
                            if (result != 0) {
                                error "Unit tests failed"
                            }
                        }
                    }
                }
                stage('E2E Tests') {
                    steps {
                        script {
                            def result = sh(script: 'python e2e.py', returnStatus: true)
                            if (result != 0) {
                                error "E2E tests failed"
                            }
                        }
                    }
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    docker.compose.down()
                    docker.image("${IMAGE_NAME}").push("${IMAGE_TAG}")
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Cleaning up...'
                docker.compose.down()
            }
        }
        success {
            script {
                echo 'Pipeline succeeded!'
            }
        }
        failure {
            script {
                echo 'Pipeline failed!'
            }
        }
    }
}
