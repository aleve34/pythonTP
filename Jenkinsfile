pipeline {
    agent any
    environment {
        CONTAINER_ID = ''
        SUM_PY_PATH = './app/sum.py'
        DOCKERFILE_PATH = './'
        TEST_FILE_PATH = './test_variables.txt'
    }
stage('Build') {
    steps {
        script {
            bat 'docker build -t sum-image .'
        }
    }
}}