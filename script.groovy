def buildApp() {
    echo 'Building Application from External Groovy Scripts...'
}

def testApp() {
    echo 'Testing Application from External Groovy Scripts...'
}

def deployApp() {
    echo 'Deploying Application from External Groovy Scripts...'
}

def deployDockerHub() {
    echo 'Deploying Application to Dockerhub from External Groovy Scripts...'
    withCredentials([usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
        sh 'docker build -t amegavi08/python_trial:my-python-app .'
        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME -password-stdin" "
        sh 'docker push amegavi08/python_trial:my-python-app'
    }

}

return this  // Returns the script's methods to the caller (Jenkinsfile)