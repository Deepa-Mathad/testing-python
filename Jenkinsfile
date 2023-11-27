

def dsau() {
  command = """ """
  command = command + "python hello.py"

  echo command
  sh command
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
