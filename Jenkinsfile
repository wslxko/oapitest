node {
   // Mark the code checkout 'stage'....
   stage 'Checkout'

   // Get some code from a GitHub repository
    git([url: 'https://github.com/wslxko/oapitest.git', branch: 'master'])

   // Mark the code build 'stage'....


    // Mark the code run 'stage'....
   stage 'Run'
   // Run the program
   bat 'python3 runtest.py'
}