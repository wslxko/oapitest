node {
        stage('checkout') {
                git([url: 'https://github.com/wslxko/oapitest.git', branch: 'master'])
        }
        stage('Test') {

                bat runner.py
        }
    }

