

def dsau() {
  try{
    
    command = """ """
    command = command + "python hello.py "
    
    // Print the command (optional)
    echo "Running command: ${command}"

    // Execute the command and capture the return value
    def returnValue = bat(script: command, returnStatus: true, returnStdout: true).trim()

    // Print the return value
    echo "Return Value: ${returnValue}"
    // echo command
    // bat command
  }
  catch (e)
    {
        // println("Failed in running DSAU", e)
        error("Exceptions with ${e}")
        return e
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
             echo "My Variable Value: ${myFunc}"
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
