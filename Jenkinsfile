pipeline {
    agent any

    stages {

         stage ('Unit Tests') {
            steps {
                bat """

                    TEST.py
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
