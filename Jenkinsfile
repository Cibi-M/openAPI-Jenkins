pipeline {
    agent any

    environment {
        // Optional — helps you see logs more clearly
        PYTHONUNBUFFERED = '1'
    }

    stages {

        stage('Preparation') {
            steps {
                echo '📦 Checking workspace and Python environment...'
                sh '''
                    pwd
                    ls -la
                    python3 --version || echo "Python3 not found!"
                    pip3 --version || echo "pip3 not found!"
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📥 Installing Python dependencies...'
                sh '''
                    pip3 install --upgrade pip
                    pip3 install jsonschema requests
                '''
            }
        }

        stage('Validate OpenAPI Spec') {
            steps {
                echo '🔍 Validating OpenAPI snapshot against expected spec...'
                sh '''
                    # List workspace contents for clarity
                    ls -la

                    # Run the validation script
                    python3 validate_with_readme.py openapi_snapshot.json openapi_expected.json
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Validation pipeline completed successfully.'
        }
        failure {
            echo '❌ Validation pipeline failed. Check the console logs for details.'
        }
    }
}
