pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Generate Expected Spec') {
            steps {
                sh './generate_spec.sh'
            }
        }

        stage('Validate OpenAPI Schema') {
            steps {
                sh '. venv/bin/activate && python validate_with_readme.py openapi_snapshot.json openapi_expected.json'
            }
        }
    }

    post {
        success {
            echo '✅ Validation Passed - OpenAPI schema matches expected.'
        }
        failure {
            echo '❌ Validation Failed - Schemas differ.'
        }
    }
}
