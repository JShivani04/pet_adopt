pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "shivanij454/pet-adoption-portal:latest"
        KUBE_DEPLOYMENT = "pet-adoption-deployment"
        DOCKER_USERNAME = "shivanij454"
        DOCKER_PASSWORD = "Logan@2020" // exposed in Jenkinsfile
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/shivanij454/pet-adoption-portal.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub using username/password
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply deployment and service YAML files from project root
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                    
                    // Wait for rollout to complete
                    sh "kubectl rollout status deployment/$KUBE_DEPLOYMENT"
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Build or deployment failed.'
        }
    }
}
