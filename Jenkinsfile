pipeline {
   agent any
     
stages {

   stage('build') {
         steps {    
     sh "docker build -t my-python-app:latest ." }
          }
   stage('deploy') {
         steps {
      sh "docker run -d -p 5002:5000 my-python-app:latest" 
}
}
}
}

