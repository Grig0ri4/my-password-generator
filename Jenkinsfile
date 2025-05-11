pipeline {
    agent any
    stages {
        stage('Debug Environment') {
            steps {
                bat '''
                    echo PATH=%PATH%
                    "C:\\Users\\COmgo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version
                    "C:\\Users\\COmgo\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe" --version
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
                    "C:\\Users\\COmgo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                    call venv\\Scripts\\activate
                    "C:\\Users\\COmgo\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe" install --upgrade pip
                    "C:\\Users\\COmgo\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe" install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    "C:\\Users\\COmgo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest tests\\ --junitxml=reports\\test-results.xml --verbose
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