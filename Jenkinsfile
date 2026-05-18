pipeline {
    agent any

    environment {
        GITHUB_CODE_REPO_URL = 'https://github.com/shivamdhang16/dockerapp'
        GITHUB_CODE_BRANCH   = 'main'
        GITHUB_REPO_CRED     = 'git-creds-sd'

        DOCKER_TAG   = "${BUILD_NUMBER}"
        DOCKER_IMAGE = "shivam5252/dockerapp"
    }


    parameters {
        choice(
            name: 'BRANCH',
            choices: ['dev', 'main'],
            description: 'Select Git branch'
        )
    }

    stages {

        stage("Checkout From Git") {
            steps {
                git branch: "${params.BRANCH}",
                    url: "${GITHUB_CODE_REPO_URL}",
                    credentialsId: "${GITHUB_REPO_CRED}"
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
                docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                '''
            }
        }

        stage("Push To Docker Hub") {
            steps {
                sh '''
                docker push $DOCKER_IMAGE:$DOCKER_TAG
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

        // stage("Run Docker Container") {
        //     steps {
        //         sh '''
        //         docker run -d \
        //         --name appcontainer \
        //         -p 5000:5000 \
        //         $DOCKER_IMAGE:$DOCKER_TAG
        //         '''
        //     }
        // }

        stage("Deploy Using Docker Compose") {
            steps {

                 sh '''
                export TAG=${BUILD_NUMBER}

                docker-compose down || true
                docker-compose pull
                docker-compose up -d
        '''
            }
        }
    }
}
