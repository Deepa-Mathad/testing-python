

def dsau() {
  try{
    
    command = """ """
    command = command + "python hello.py "
    command = command + "pip install requests"
  
    echo command
    bat command
  }
  catch (e)
    {
        println("Failed in running DSAU", e)
        error("Exceptions with ${e}")
    }
}


pipeline {
  agent any
  stages {
    // stage('hello') {
    //   steps {
    //      script {
    //                 catchError(buildResult: 'FAILURE') {
    //                     bat 'hello.py'
    //                 }
    //             }
    //   }
    // }
     stage('Test') {
        steps {
          script {
             def myFunc = dsau()
             println("Result",myFunc)
          }
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
