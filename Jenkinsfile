pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
         script {
                    catchError(buildResult: 'FAILURE') {
                        bat 'hello.py'
                        echo 'set'
                    }
                }
      }
      stage('Test') {
        steps {
             bat 'hello.py'
         }
      }
    }
  }
}
