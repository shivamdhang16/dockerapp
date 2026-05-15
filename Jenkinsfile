pipeline{
    agent any
    stages{
        stage("checkoutfromgit"){
            steps{
               git branch: 'main', url: 'https://github.com/shivamdhang16/dockerapp', credentialsId: 'git-creds-sd'
            }
            }
        stage("build image"){
            steps{
                sh '''docker build -t appimage .'''
            }
        }

        stage("Docker container creat"){
            steps{
                sh ''' docker run -d --name appcontainer -p 5000:5000 appimage'''
            }
        }
        }
  }

