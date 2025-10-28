pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Installing required system packages (without sudo)...'
                sh '''
                    set -e
                    apt-get update -y
                    apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-venv python3-pip
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                echo 'Creating Python virtual environment...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    python --version
                    pip install --upgrade pip setuptools wheel
                '''
            }
        }

        stage('Install Requirements') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up virtual environment...'
                sh '''
                    rm -rf ${VENV_DIR}
                '''
            }
        }
    }

    post {
        always {
            echo 'Build completed.'
        }
        failure {
            echo 'Build failed.'
        }
        success {
            echo 'Build succeeded.'
        }
    }
}
