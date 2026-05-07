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
                    ./test/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            parallel {
                stage('Lint') { steps { sh "./${VENV}/bin/flake8 ." } }
                stage('Unit Tests') { steps { sh "./${VENV}/bin/pytest" } }
            }
        }
    }
}