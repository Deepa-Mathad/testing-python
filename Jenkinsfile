

def dsau() {
  try {
    command = """python test.py"
                  python extraStep.py
    """
    
    // Print the command (optional)
    echo "Running command: ${command}"

    // Execute the command and capture the return value
    try{
      // def combinedCommand = "${command} 2>&1"
      def returnValue = bat(script: dir, returnStdout: true)
      echo returnValue
      //def stderr = bat(script: combinedCommand, returnStatus: true)
      // return returnValue
   } catch (Exception e) {
      echo "Cause: ${e}"
      return e
    }

    // def returnValue1 = bat(script: 'python test.py', returnStatus: true, returnStdout: true)
    // if(returnValue1 != 0){
    //   echo "Return Value: ${returnValue1}"
    //   return returnValue1
    // }
    // else{
    //   def returnValue2 = bat(script: 'python extraStep.py', returnStatus: true, returnStdout: true)
    // }

    // Print the return value
   // echo "Return Value: ${returnValue}"

    // Return the value
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
                        error "Stage failed"
                        return
                        // skipRemainingStages = true
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
