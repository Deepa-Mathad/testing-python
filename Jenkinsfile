pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
		script {
			try {
				def branchName = env.BRANCH_NAME == 'main'
				echo "compare: ${branchName}"
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
