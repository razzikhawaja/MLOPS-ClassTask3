pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = credentials('docker-credentials') 
        DOCKER_HUB_PASSWORD = credentials('docker-credentials')  
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/razzikhawaja/MLOPS-ClassTask3.git'
            }
        }

        stage('Set up Docker Buildx') {
            steps {
                sh 'docker buildx create --use'
            }
        }

        stage('Log in to Docker Hub') {
            steps {
                sh """
                echo ${DOCKER_HUB_PASSWORD} | docker login -u ${DOCKER_HUB_USERNAME} --password-stdin
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    sh "docker build -t ${DOCKER_HUB_USERNAME}/ml-app:${commitId} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    sh "docker push ${DOCKER_HUB_USERNAME}/ml-app:${commitId}"
                }
            }
        }
    }

    post {
        always {
            // Clean up images after the build is done
            sh "docker rmi $(docker images -q)"
        }
    }
}
