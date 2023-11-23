

def dsau() {
  bat 'hello.py'
}


pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
         script {
                    catchError(buildResult: 'FAILURE') {
                        bat 'hello.py'
                    }
                }
      }
    }
     stage('Test') {
        steps {
             dsau()
         }
      }
  }
  post{
        // always cleanup
        always{
            deleteDir()
        }
    }
}
