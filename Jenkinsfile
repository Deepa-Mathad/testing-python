pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
		try {
			errorCode = bat( label: '', returnStdout: true, script: """
			bat 'hello.py'
			
			IF NOT %ERRORLEVEL% == 0 ( 
				echo "ABORT: " %ERRORLEVEL%
				exit /b %ERRORLEVEL%
			  )
			""")
		}
		catch (e)
		{
			error("Tests didn't finish successfully: ${e}")
		}
      }
    }
  }
}
