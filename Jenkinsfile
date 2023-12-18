pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
		script {
			try {
				errorCode = bat( label: '', returnStdout: true, script: """
				bat 'hello.py
        echo "banch name: ${env.BRANCH_NAME}"
			}
			catch (e)
			{
				error("Tests didn't finish successfully: ${e}")
			}
		}
      }
    }
  }
}
