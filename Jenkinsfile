pipeline {
    agent any

    stages {

         stage ('Unit Tests') {
            steps {
                bat """

                    pytest
                """
            }


        }
        stage('SonarQube Analysis'){
            steps {
                script{
                    scannerHome = tool'SonarQube'
                }
                withSonarQubeEnv('Sonar-server'){
                    bat"${scannerHome}/bin/Sonar-scanner"
                }
            }
        }

    }
}