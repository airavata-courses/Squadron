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
              session = docker.build("squadronteam/session:${env.BUILD_ID}","./session.management")
              data = docker.build("squadronteam/data:${env.BUILD_ID}", "./DataRetrieval")
              model = docker.build("squadronteam/model:${env.BUILD_ID}", "./ModelService")
              post = docker.build("squadronteam/post:${env.BUILD_ID}", "./PostProcessing")
              user = docker.build("squadronteam/user:${env.BUILD_ID}", "./user_management")
              api = docker.build("squadronteam/api:${env.BUILD_ID}", "./api_gateway")

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
          data.inside('-u root --privileged') {
            sh 'cd /app/handlers; GOCACHE=/tmp/cache CGO_ENABLED=0 go test'
          }
        }
      }
    }
    stage('Push docker images'){
      steps {
        echo 'Pushing docker images to the repository'
        script {
          docker.withRegistry('https://registry.hub.docker.com', 'docker-credentials'){
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
