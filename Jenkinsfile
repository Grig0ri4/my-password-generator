pipeline {
    agent any
    stages {
        stage('Debug Environment') {
            steps {
                bat '''
                    echo PATH=%PATH%
                    python --version
                    pip --version
                '''
            }
        }
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Grig0ri4/my-password-generator.git', branch: 'main'
            }
        }
        stage('Setup Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest tests\\ --junitxml=reports\\test-results.xml --verbose
                '''
            }
            post {
                always {
                    junit 'reports/test-results.xml'
                }
            }
        }
    }
}