def buildApp() {
    echo 'Building Application from External Groovy Scripts...'
}

def testApp() {
    echo 'Testing Application from External Groovy Scripts...'
}

def deployApp() {
    echo 'Deploying Application from External Groovy Scripts...'
}

return this  // Returns the script's methods to the caller (Jenkinsfile)