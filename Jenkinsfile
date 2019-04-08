node('docker') {
    checkout scm
    stage('Build') {
        docker.image('python:3.7.0').inside {
            sh 'python --version'
        }
    }
}