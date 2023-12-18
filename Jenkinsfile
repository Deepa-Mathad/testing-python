pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
		script {
			try {
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
