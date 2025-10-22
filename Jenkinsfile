// Poll SCM test change
//Second time change for Poll SCM
//Third time change for Poll SCM
pipeline {
    agent any

    environment {
        // 🔧 Replace with your actual Docker Hub username
        DOCKER_HUB_USER = 'shivanij454'
        IMAGE_NAME = 'pet_adoption_app'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo '📥 Checking out code from GitHub...'
                git 'https://github.com/JShivani04/pet_adopt.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                bat "docker build -t %DOCKER_HUB_USER%/%IMAGE_NAME%:latest ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                echo '🔑 Logging into Docker Hub...'
                // ⚠️ Replace 'Logan@2020' with your Docker Hub password
                bat "echo Logan@2020 | docker login -u %DOCKER_HUB_USER% --password-stdin"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo '📤 Pushing Docker image to Docker Hub...'
                bat "docker push %DOCKER_HUB_USER%/%IMAGE_NAME%:latest"
            }
        }

        stage('Deploy Container') {
            steps {
                echo '🚀 Running Docker container...'
                bat "docker stop petapp-container || exit 0"
                bat "docker rm petapp-container || exit 0"
                bat "docker run -d -p 5000:5000 --name petapp-container %DOCKER_HUB_USER%/%IMAGE_NAME%:latest"
            }
        }
    }

    post {
        success {
            echo '✅ Build and Deployment Successful!'
        }
        failure {
            echo '❌ Pipeline Failed. Check logs for errors.'
        }
    }
}
