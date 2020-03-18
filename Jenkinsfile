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
        sh "docker build -t squadronteam/session ./session.management"
      }
    }

    stage('Run unit test cases'){
      steps{
        sh "docker run squadronteam/session /bin/bash -c "mvn test""
      }
    }

  }

}