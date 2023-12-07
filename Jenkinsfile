

def dsau() {
  try {
    command = """python test.py
                  python extraStep.py
    """
    
    // Print the command (optional)
    echo "Running command: ${command}"

    // Execute the command and capture the return value
    try{
      // def combinedCommand = "${command} 2>&1"
      def returnValue = bat(returnStderr: true, script: command)
      echo "returnValue: ${returnValue}"
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
    stage('hello') {
      steps {
                script {
                    def logFilePath1 = "${WORKSPACE}/output1.log"
                    def logFilePath2 = "${WORKSPACE}/output2.log"
                    // Define the combined command
                    def combinedCommand = """
                        python test.py > ${logFilePath1}
                        python extraStep.py > ${logFilePath2}
                    """

                    // Run the combined command and capture the output
                    //def combinedOutput = bat(returnStdout: true, script: combinedCommand)

                    bat(script: combinedCommand)
                    echo "Log File Path: ${logFilePath1}"
                    echo "Log File Path: ${logFilePath2}"
                    def fullOutput1 = readFile(logFilePath1)
                    def fullOutput2 = readFile(logFilePath2)
                    echo "Full Output1:\n${fullOutput1}"
                    echo "Full Output1:\n${fullOutput2}"
                    // Print the combined output
                    //echo "Combined Output: ${combinedOutput}"

                    // Add further processing based on the output if needed
                }
            }
    }
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
