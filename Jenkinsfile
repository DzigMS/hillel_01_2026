pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git "https://github.com/DzigMS/hillel_01_2026.git"
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
            steps {
                sh "./${VENV}/bin/pytest"
            }
        }
    }
}