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
      stage('hello') {
      steps {
         steps{
           bat 'hello.py'
         }
      }
    }
  }
}
