

def dsau() {
  try {
    command = """python extraStep.py
                 python test.py
    """
    
    // Print the command (optional)
    echo "Running command: ${command}"

    // Execute the command and capture the return value
    //def returnValue = bat(script: command, returnStatus: true, returnStdout: true)

    def returnValue1 = bat(script: 'python test.py', returnStatus: true, returnStdout: true)
    if(returnValue1 != 0){
      echo "Return Value: ${returnValue1}"
      return returnValue1
    }
    else{
      def returnValue2 = bat(script: 'python extraStep.py', returnStatus: true, returnStdout: true)
    }

    // Print the return value
   // echo "Return Value: ${returnValue}"

    // Return the value
   // return returnValue
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
             if (myFunc == 0) {
                        echo "Stage succeeded"
                        currentBuild.result = 'SUCCESS'
                    } else {
                        echo "Stage failed"
                        currentBuild.result = 'FAILURE'
                        skipRemainingStages = true
                    }
          }
         }
      }
    stage('Upload database to artifactory'){
            steps{
                echo "Uploaded DB to artifactory"
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
