node {
   // Mark the code checkout 'stage'....
   stage 'Checkout'

   // Get some code from a GitHub repository
    git([url: 'https://github.com/wslxko/oapitest.git/', branch: 'master'])

   // Mark the code build 'stage'....


    // Mark the code run 'stage'....
   stage 'Run'
   // Run the program
   export PATH=/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/bin
   python3 runner.py