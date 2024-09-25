pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = credentials('dockerhub-credenials')  
        DOCKER_HUB_PASSWORD = credentials('dockerhub-credentials')  
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone your code repository
                git branch: 'main', url: 'https://github.com/razzikhawaja/MLOPS-ClassTask3.git' // Replace with your repo URL
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
            // Clean up docker images after the build
            sh 'docker rmi $(docker images -q)'
        }
    }
}
