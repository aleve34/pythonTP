pipeline {
    agent any
    environment {
        CONTAINER_ID = ''
        SUM_PY_PATH = './app/sum.py'
        DOCKERFILE_PATH = './'
        TEST_FILE_PATH = './test_variables.txt'
    }
    stages { 
        stage('Build') {
            steps {
                script {
                    bat 'docker build -t sum-image .'
                }
            }
        }
    }
    stage('Run') {
    steps {
        script {
            def output = bat(script: 'docker run -d sum-image', returnStdout: true).trim()
            def lines = output.split('\n')
            CONTAINER_ID = lines[-1].trim()
            echo "Conteneur lancé avec l'ID : ${CONTAINER_ID}"
        }
    }
}
}

