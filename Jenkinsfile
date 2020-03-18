pipeline {

  environment {
    registry = "192.168.1.81:5000/justme/myweb"
    dockerImage = ""
  }

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git 'https://github.com/airavata-courses/Squadron.git'
      }
    }
    stage('Build docker images') {
      steps {
       echo 'Starting to build docker images of build ${env.BUILD_ID} in workspace ${env.WORKSPACE}'
       script {
              def session = docker.build("squadronteam/session:${env.BUILD_ID}","-f ${env.WORKSPACE}/session.management/Dockerfile .")
        }
      }
    }
  }

}
