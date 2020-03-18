pipeline {

  environment {
    registry = "192.168.1.81:5000/justme/myweb"
    dockerImage = ""
  }

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git branch: 'develop', url: 'https://github.com/airavata-courses/Squadron.git'
      }
    }
    stage('Build docker images') {
      steps {
       echo 'Starting to build docker images'
       script {
              def session = docker.build("squadronteam/data","./DataRetrieval")
        }
      }
    }
  }

}
