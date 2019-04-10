node {
   stage 'Checkout'
   git([url: 'https://github.com/wslxko/oapitest.git/', branch: 'master'])
   stage 'Run'
   export PATH='/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/bin'
   python3 runner.py
}