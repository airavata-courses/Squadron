pipeline {

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
              session = docker.build("squadronteam/session","./session.management")
              data = docker.build("squadronteam/data", "./DataRetrieval")
        }
      }
    }
    stage('Run test cases') {
      steps {
        echo ' Running test cases'
        script {
          session.inside {
            sh 'cd session.management; mvn test'
          }
        }
      }
    }
    stage('Push docker images'){
      steps {
        echo 'Pushing docker images to the repository'
        script {
          docker.withRegistry('https://registry.hub.docker.com', '047c1f6d-ef5a-440c-9e89-6a5e895d618d'){
            session.push()
            data.push()
          }
        }
      }
    }
  }

}
