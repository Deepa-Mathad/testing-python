def getBranchName(){
    String cron_string = env.GIT_BRANCH == 'main' ? 'TZ=US/Pacific\nH 17 * * *' : ''
    return cron_string
}
pipeline {
  agent any
  triggers {
     cron(getBranchName())
  }
  stages {
    stage('hello') {
      steps {
		script {
			try {
				def branchName = env.BRANCH_NAME == 'main'
				echo "compare: ${branchName}"
				echo "banch name: ${env.BRANCH_NAME}"
				def cronBranch = getBranchName()
				echo "cronBranch: ${cronBranch}"
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
