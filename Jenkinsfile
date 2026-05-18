pipeline{
    agent any
    environment {
    GITHUB_CODE_REPO_URL = 'https://github.com/shivamdhang16/dockerapp'
    GITHUB_CODE_BRANCH  =  'main'
    GITHUB_REPO_CRED    = 'git-creds-sd'
    DOCKER_TAG     = "${BUILD_NUMBER}"
    DOCKER_IMAGE = "shivam5252/dockerapp"


   }
    stages{
        stage("checkoutfromgit"){
            steps{
               git branch: $GITHUB_CODE_BRANCH, url: $GITHUB_CODE_REPO_URL, credentialsId: $GITHUB_REPO_CRED
            }
            }
        stage("docker login"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                     sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
        stage("Push Image") {
            steps {
                sh '''
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }
            }
        }
        stage("build image"){
            steps{
                sh '''docker build -t appimage .'''
            }
        }
        stage("push to docker hub")
            steps{
                sh ''''''
            }

        stage("Docker container creat123"){
            steps{
                sh ''' docker run -d --name appcontainer -p 5000:5000 appimage'''
            }
        }
        }
  }

