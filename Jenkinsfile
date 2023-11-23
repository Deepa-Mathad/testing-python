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
             bat 'hello.py'
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
