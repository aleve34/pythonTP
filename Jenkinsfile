pipeline {
    agent any
    environment {
        CONTAINER_ID = ''
        SUM_PY_PATH = '/app/sum.py'
        DOCKERFILE_PATH = './'
        TEST_FILE_PATH = './test_variables.txt'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    bat 'docker build -t sum-image .' // Build the Docker image
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Clean up existing containers
                    bat 'docker rm -f sum-container || true'
                    
                    // Run a new container in the background
                    def output = bat(script: 'docker run -d --name sum-container sum-image tail -f /dev/null', returnStdout: true).trim()
                    CONTAINER_ID = output.split('\n')[-1].trim()
                    echo "Conteneur lancé avec l'ID : ${CONTAINER_ID}"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Read the test data from the file
                    def testLines = readFile(TEST_FILE_PATH).split('\n')
                    for (line in testLines) {
                        def vars = line.split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()

                        // Execute the Python script inside the container and capture the output
                        def output = bat(script: "docker exec ${CONTAINER_ID} python ${SUM_PY_PATH} ${arg1} ${arg2}", returnStdout: true).trim()

                        // Extract just the result (the sum) from the output, removing any leading command parts
                        def result = output.tokenize().last().toFloat() // This assumes the sum is the last token in the output

                        // Ensure the result is as expected
                        if (result == expectedSum) {
                            echo "Test réussi pour ${arg1} + ${arg2} = ${expectedSum}"
                        } else {
                            error "Test échoué pour ${arg1} + ${arg2}. Résultat attendu : ${expectedSum}, obtenu : ${result}"
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                // Clean up the container after the pipeline
                if (CONTAINER_ID) {
                    bat "docker stop ${CONTAINER_ID}"
                    bat "docker rm ${CONTAINER_ID}"
                    echo "Conteneur ${CONTAINER_ID} arrêté et supprimé."
                }
            }
        }
    }
}
