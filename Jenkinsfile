pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout 'https://github.com/DzigMS/hillel_01_2026.git'
            }
         }
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv test
                    ./test/bin/pip install -r lesson_26/requirements.txt
                '''
            }
        }
        stage('Test') {
            stage('Unit Tests') {
                steps {
                    sh "./${VENV}/bin/pytest"
                }

        }
    }
}