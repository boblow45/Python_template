// ------------------------ Variables used by the Jenkins Script ------------------------
// Defines the location of where to place the generated documentation
env.MODULE_NAME = 'Project_template'

def eMailList = '$DEFAULT_RECIPIENTS, cillianobrien01@gmail.com'

def successEMail = """
${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}
More info at: ${env.BUILD_URL}

To see the changes and updates to the module please refer to the attached changelog.
Documentation on this module can be found here: ${env.BUILD_URL}Module_20Documentation/
Examples of how to use the module can be found here: 
"""

def getVersion(){

	sh(script: """python -c 'print(open("setup.cfg", "r").readlines()[1].replace(" ","").split("=")[-1])'""")
}

def checkVersionIsValid(){ 
   
   sh(script: """python -c 'import subprocess
pypi_server = "${SERVER_LOC}"
package = "${env.MODULE_NAME}"
command = "pip search -i {} {}".format(pypi_server, package)
new_version = "${VERSION_NUM}"

try:
	cmd_ans = str(subprocess.check_output(command, shell=True))
	server_version = list(map(int, cmd_ans[cmd_ans.find("(") + 1:cmd_ans.find(")")].split(".")))
	package_version = list(map(int, new_version.split(".")))
except:
	exit(0)

print("Server version is {}".format(server_version))
print("Package version is {}".format(package_version))

for ser_ver, pac_ver in zip(list(server_version), list(package_version)):
	if pac_ver > ser_ver:
		print("Package version number is larger")
		exit(0)
	elif pac_ver < ser_ver:
		print("Server number is larger")
		exit(1)
		break
	else:
		pass
else:
	print("Server number is larger")
	exit(1)
'""")
}

// ------------------------------ Jenkins Pipeline Script ----------------------------
pipeline {
	agent { docker{
				image 'python:3.6'
				label 'docker'
			}
		}
    triggers {
        pollSCM('H/5 * * * 1-5')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    environment {
        VERSION_NUM = '0.0.0'
		SERVER_LOC = 'Fill this in'
    }

	stages {
		stage('Build environment') {
			steps {
				sh "make install-dev"

				script {

					VERSION_NUM = getVersion()
				}
			}
		}
		stage('Test environment') {
			steps {
				sh '''
					make test
					'''

			}
		}

		stage("Test Module Version"){
        	when {
                branch 'PR-*'  
            }

			steps{
				
				// This will error out if version number of package is the same or less. Need to add a message to the console 
				checkVersionIsValid()
			}
		}

	}

    // The following section is ran after the above pipeline has finished weither it passes or fails 
    post {

        // The following section will be preformed if the pipeline runs without issues 
		success {
	            echo 'The project build and deployed correctly!'

                emailext(subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
					     attachmentsPattern: '**/Changelog.md',
						 body: "${successEMail}",
						recipientProviders: [
							[$class: 'CulpritsRecipientProvider'],
							[$class: 'DevelopersRecipientProvider'],
							[$class: 'RequesterRecipientProvider'],
						],
						replyTo: '$DEFAULT_REPLYTO',
						to: eMailList,
					)
		}

        // The following section will run if an error has occur. It will inform the admin and the person who caused the issue
		failure {
			echo 'The project build and deployed correctly!'

			emailext( subject: '$DEFAULT_SUBJECT',
				body: '$DEFAULT_CONTENT',
				recipientProviders: [
					[$class: 'CulpritsRecipientProvider'],
					[$class: 'DevelopersRecipientProvider'],
					[$class: 'RequesterRecipientProvider']
				],
				replyTo: '$DEFAULT_REPLYTO',
				to: eMailList,
			)
		}

        // This section will run regardless of what has happed.
        always {
            junit 'tests/pytest_output/test_results.xml'
        }
    }

}
