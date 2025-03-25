def groovy

pipeline {
    agent any

    stages {


        stage('Initialize') {

                steps {

                    scripts {
                         groovy = load 'script.groovy'
                    }

                }

        }

        stage('Build') {

                steps {
                    scripts {
                         groovy.buildApp()
                    }
                }

        }

        stage('Test') {

                steps {
                    scripts {
                         groovy.testApp()
                    }
                }

        }

        stage('Deploy') {

                steps {
                    scripts {
                         groovy.deployApp()
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