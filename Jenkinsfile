pipeline {
    agent any

    //  agent {
    //     label 'docker'
    // } 

    environment {
        DOCKER_TAG   = "${BUILD_NUMBER}"
        DOCKER_IMAGE = "shivam5252/dockerapp"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Show Branch') {
            steps {
                echo "Current branch is: ${env.BRANCH_NAME}"
            }
        }

        stage("Docker Login") {
            steps {

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage("Build Docker Image") {
            steps {

                sh '''
                docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                '''
            }
        }

        stage("Push To Docker Hub") {
            steps {

                sh '''
                docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                '''
            }
        }

        stage("Remove Old Container") {
            steps {

                sh '''
                docker rm -f appcontainer || true
                '''
            }
        }

        stage("Deploy Container") {
            steps {

                sh '''
                docker run -d \
                --name appcontainer \
                -p 5000:5000 \
                ${DOCKER_IMAGE}:${DOCKER_TAG}
                '''
            }
        }

        stage ("compliting all step")

         echo "all steps done"
    }

    post {

        success {
            echo "Build and Deployment Successful"
        }

        failure {
            echo "Pipeline Failed"
        }

        always {
            sh 'docker logout'
        }
    }
}
