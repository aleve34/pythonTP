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
                    bat 'docker build -t sum-image .' // Construire l'image Docker
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    // Nettoyer les conteneurs existants
                    bat 'docker rm -f sum-container || true'
                    
                    // Lancer un conteneur actif
                    def output = bat(script: 'docker run -d --name sum-container sum-image tail -f /dev/null', returnStdout: true).trim()
                    CONTAINER_ID = output.split('\n')[-1].trim()
                    echo "Conteneur lancé avec l'ID : ${CONTAINER_ID}"
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Lecture du fichier de test
                    def testLines = readFile(TEST_FILE_PATH).split('\n')
                    for (line in testLines) {
                        def vars = line.split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()

                        // Exécuter le script Python dans le conteneur
                        def output = bat(script: "docker exec ${CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}", returnStdout: true).trim().split('\n')[0]


                        // Vérifier le résultat
                        def result = output.toFloat()
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
}
