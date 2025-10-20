pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "shivanij454/pet-adoption-portal:latest"
        DOCKER_USERNAME = "shivanij454"
        DOCKER_PASSWORD = "Logan@2020"  // For testing only; use Jenkins credentials in production
        KUBE_DEPLOYMENT = "pet-adoption-deployment"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/shivanij454/pet-adoption-portal.git'
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
            echo '✅ CI/CD pipeline successful! Docker image built, pushed, and deployed to Kubernetes.'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for errors.'
        }
    }
}
