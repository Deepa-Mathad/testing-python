

def dsau() {
  try {
    command = """python test.py"""
    
    // Print the command (optional)
    echo "Running command: ${command}"

    // Execute the command and capture the return value
    def returnValue = bat(script: command, returnStatus: true, returnStdout: true)

    // Print the return value
    echo "Return Value: ${returnValue}"

    // Return the value
    return returnValue
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
             if (myFunc = 0) {
                        echo "Stage succeeded"
                        currentBuild.result = 'SUCCESS'
                    } else {
                        echo "Stage failed"
                        currentBuild.result = 'FAILURE'
                        error "Stage failed"
                    }
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
