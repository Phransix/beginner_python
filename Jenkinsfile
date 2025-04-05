def gv  // Global variable to hold loaded script methods

pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                script {
                    gv = load "script.groovy"  // Load external Groovy script
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    gv.buildApp()  // Call buildApp() from loaded script
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    gv.testApp()  // Call testApp() from loaded script
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    gv.deployApp()  // Call deployApp() from loaded script
                }
            }
        }

        stage('Deploy to DockerHub') {
            steps {
                script {
                    gv.deployDockerHub()  // Call deployDockerHub() from loaded script
                }
            }
        }

        stage('Connect to ec2 instance') {
            steps {
                script {
                    def dockerCmd = 'docker run -d -p 3005:3005 <name-of-your-image>'
                    sshagent(['heavy_dealers']) {
                      sh 'echo "EC2 instance login setup"'
                      sh "ssh -o StrictHostKeyChecking=no ec2-user@<ec2-public-ip> ${dockerCmd}"
                    }
                }
            }
        }

    }

    post {
        always {
            script {
                // Send email notification (requires Email Extension Plugin)
                emailext (
                    subject: "Jenkins Pipeline - Build #${env.BUILD_NUMBER}",
                    body: """<p>Build #${env.BUILD_NUMBER} of ${env.JOB_NAME} has finished with status: ${currentBuild.currentResult}</p>
                             <p>Check the details <a href="${env.BUILD_URL}">here</a></p>""",
                    to: "$EMAIL_RECEPIENTS",  // Ensure this variable is set
                    mimeType: 'text/html'
                )
            }
        }
    }
}
