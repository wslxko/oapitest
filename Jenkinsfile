node {
   stage 'Checkout'
   git([url: 'https://github.com/wslxko/oapitest.git/', branch: 'master'])
   stage 'Run'
   python3 runner.py
}