pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.13'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Installing required system packages...'
                sh '''
                    set -e
                    sudo apt-get update -y
                    sudo apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-venv python3-pip
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
                echo 'Installing Python dependencies...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests using pytest...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Cleaning up workspace...'
                sh '''
                    deactivate || true
                    rm -rf ${VENV_DIR}
                '''
            }
        }
    }

    post {
        always {
            echo 'Build completed. Cleaning up temporary files.'
        }
        failure {
            echo 'Build failed. Please check logs above for errors.'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
