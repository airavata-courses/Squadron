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
              model = docker.build("squadronteam/model", "./ModelService")
              post = docker.build("squadronteam/post", "./PostProcessing")
              user = docker.build("squadronteam/user", "./user_management")
              api = docker.build("squadronteam/api", "./api_gateway")

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
          model.inside {
            sh 'cd ModelService; python modeltest.py'
          }
          user.inside {
            sh 'cd user_management; user_management/manage.py test api -v 2'
          }
          post.inside {
            sh 'cd PostProcessing; python testPP.py'
          }
          data.inside {
            sh 'pwd && cd /app && go mod tidy'
            //sh 'cd /app/handlers; GOCACHE=/tmp/cache CGO_ENABLED=0 go test'
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
            model.push()
            post.push()
            user.push()
            api.push()
          }
        }
      }
    }
  }

}
