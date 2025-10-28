pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'  // ensures real-time log output
    }

    stages {

        stage('Preparation') {
            steps {
                echo '📦 Checking workspace and Python environment...'
                sh '''
                    echo "Current working directory:"
                    pwd
                    echo "Listing files in workspace:"
                    ls -la

                    echo "Checking Python versions:"
                    python3 --version || echo "Python3 not found!"
                    pip3 --version || echo "pip3 not found!"
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                echo '🐍 Creating Python virtual environment...'
                sh '''
                    # Remove any existing venv
                    rm -rf venv
                    
                    # Create and activate virtual environment
                    python3 -m venv venv

                    # Upgrade pip safely inside venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📥 Installing Python dependencies...'
                sh '''
                    . venv/bin/activate
                    pip install jsonschema requests
                '''
            }
        }

        stage('Validate OpenAPI Spec') {
            steps {
                echo '🔍 Running OpenAPI validation script...'
                sh '''
                    . venv/bin/activate
                    ls -la  # show that the JSON and scripts exist
                    python validate_with_readme.py openapi_snapshot.json openapi_expected.json
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Validation pipeline completed successfully.'
        }
        failure {
            echo '❌ Validation pipeline failed. Check Jenkins logs for details.'
        }
    }
}
