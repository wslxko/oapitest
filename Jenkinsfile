node {
        stage('checkout') {
                git([url: 'https://github.com/wslxko/oapitest.git', branch: 'master'])
        }
        stage('Test') {
            step{
                scripts{
                timeout(time: 20,unit:'MINUTES'){
                bat 'python3 runtest.py'
                }
            }
        }
   }
}

