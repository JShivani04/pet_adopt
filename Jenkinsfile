pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "shivanij454/pet_adoption_app:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone public repo using HTTPS (no credentials needed)
                git branch: 'master', url: 'https://github.com/JShivani04/pet_adopt.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Log in to Docker using username & password directly
                    // ⚠️ Only if you’re okay hardcoding temporarily (not secure for production)
                    sh 'echo "Logan@2020" | docker login -u "shivanij454" --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Run the app container locally
                    sh 'docker run -d -p 8080:80 $DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Application built and running successfully!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
