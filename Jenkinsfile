node {
        stage('checkout') {
                git([url: 'https://github.com/wslxko/oapitest.git', branch: 'master'])
        }
        stage('Test') {
                export PATH=/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/bin
                bat runner.py
        }
    }

