node('docker') {
    checkout scm
    stage('Build') {
        sh 'echo "Hello World"'
        sh '''
            echo "Multiline shell steps works too"
        '''
    }

    stage('Test'){
        docker.images('python:3.7.0').inside{
            sh 'python3 runner.py'
        }
    }
}