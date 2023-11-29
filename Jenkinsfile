pipeline {
    agent any
    stages {
        stage ("scm checkout") {
               stage ("git") {
                   steps {
                       node ("setup") {
                           git credentialsId: '***********', url: 'https://github.com/suresh1298/Test'
                       }
                   }
               }
        }
        stage ("Test Cases") {
            steps {
              sh 'cd /opt/Test'
              echo 'test unittest'
              sh 'test_orders_analysis.py'
                    }
        }
        stage (" Docker buld") {
            steps {
                node ("setup") {
                    sh 'cd /opt/Test'
                    sh 'docker build -t your-task-service -f Dockerfile.task .'
                    sh 'docker build -t your-test-service -f Dockerfile.test .'
                }
            }
        }
        stage ('starting the Container') {
            steps {
                node ("setup") {
                  sh 'docker run your-task-service'
                  sh 'docker run your-test-service'
                }
            }
        }
    }
}
