pipeline {
    agent any
    environment {
        CONTAINER_ID = ''
        SUM_PY_PATH = '/app/sum.py'
        DOCKERFILE_PATH = './'
        TEST_FILE_PATH = './test_variables.txt'
        DOCKER_USERNAME = 'sirine3443'   // Docker Hub username
        DOCKER_PASSWORD = '0123.0123'   // Docker Hub password
        SPHINX_SOURCE = '/app/docs/source' // Source directory for Sphinx
        SPHINX_BUILD_DIR = '/app/docs/build' // Build output directory for Sphinx
    }
    stages {
        stage('Build') {
            steps {
                script {
                    bat 'docker build -t sum-image .' 
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    bat 'docker rm -f sum-container || true'
                    def output = bat(script: 'docker run -d --name sum-container sum-image tail -f /dev/null', returnStdout: true).trim()
                    CONTAINER_ID = output.split('\n')[-1].trim()
                    echo "Conteneur lancé avec l'ID : ${CONTAINER_ID}"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def testLines = readFile(TEST_FILE_PATH).split('\n')
                    for (line in testLines) {
                        def vars = line.split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()

                        def output = bat(script: "docker exec ${CONTAINER_ID} python ${SUM_PY_PATH} ${arg1} ${arg2}", returnStdout: true).trim()
                        def result = output.tokenize().last().toFloat() 
                        if (result == expectedSum) {
                            echo "Test réussi pour ${arg1} + ${arg2} = ${expectedSum}"
                        } else {
                            error "Test échoué pour ${arg1} + ${arg2}. Résultat attendu : ${expectedSum}, obtenu : ${result}"
                        }
                    }
                }
            }
        }
        stage('Performance Monitoring') {
            steps {
                script {
                    def stats = bat(script: "docker stats --no-stream ${CONTAINER_ID}", returnStdout: true).trim()
                    echo "Performances du conteneur ${CONTAINER_ID} : \n${stats}"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    bat "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                    bat "docker tag sum-image ${DOCKER_USERNAME}/sum-image:latest"
                    bat "docker push ${DOCKER_USERNAME}/sum-image:latest"
                }
            }
        }
        stage('Documentation') {
            steps {
                script {
                    bat "docker exec ${CONTAINER_ID} sphinx-build -b html ${SPHINX_SOURCE} ${SPHINX_BUILD_DIR}"

                    archiveArtifacts artifacts: "${SPHINX_BUILD_DIR}/**/*.html", allowEmptyArchive: true
                }
            }
        }
    }
    post {
        always {
            script {
                if (CONTAINER_ID) {
                    bat "docker stop ${CONTAINER_ID}"
                    bat "docker rm ${CONTAINER_ID}"
                    echo "Conteneur ${CONTAINER_ID} arrêté et supprimé."
                }
            }
        }
    }
}
