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
              ui = docker.build("squadronteam/ui", "./UI")

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
            ui.push()
          }
        }
      }
    }
    stage('Deploy code') {
        agent {
            kubernetes {
              label 'squadron-jenkins'
              serviceAccount 'squadron-jenkins'
              containerTemplate {
                name 'helm'
                image 'squadronteam/helm-jenkins'
                ttyEnabled true
                command 'cat'
                }
            }
        }
        
      steps {
        container('helm') {
          git url: 'git://github.com/airavata-courses/Squadron.git', branch: 'develop'
          sh '''
            pwd
            cd helm-chart
            helm dependency update squadron/
            helm list
            DEPLOYED=$(helm list |grep -E "^squadron" |grep -i DEPLOYED |wc -l)
            TIMESTAMP=$(date "+%H:%M:%S-%d/%m/%y")
            if [ $DEPLOYED == 1 ] ; then
              helm install squadron squadron/
            else
              helm upgrade squadron squadron/  --set-string timestamp=$TIMESTAMP
            fi
          echo "deployed!"
          '''
        }
      }
    }
  }
}
