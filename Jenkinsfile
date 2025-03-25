pipeline {
    agent any

    stages {

        stage('Build') {

                steps {
                    echo 'Building the application...'
                }

        }

        stage('Test') {

                steps {
                    echo 'Testing the application...'
                }

        }

        stage('Deploy') {

                steps {
                    echo 'Deploying the application...'
                }

        }

    }

     post {

    always {

// archiveArtifacts artifacts: '**/report-task.txt', allowEmptyArchive: true
  script {
    

                // Send email notification
      emailext (
                    subject: "Jenkins Pipeline - Build #${env.BUILD_NUMBER}",
                    body: """<p>Build #${env.BUILD_NUMBER} of ${env.JOB_NAME} has finished with status: ${currentBuild.currentResult}</p>
                             <p>Check the details <a href="${env.BUILD_URL}">here</a></p>""",
                    to: "$EMAIL_RECEPIENTS",
                    mimeType: 'text/html'
                )
      // cleanWs()


    
    }

    }

    }
}