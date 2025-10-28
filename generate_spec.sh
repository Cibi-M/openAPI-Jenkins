#!/bin/bash
set -e

echo "🚀 Generating OpenAPI spec..."
python manage.py spectacular --format openapi-json --file openapi_expected.json
echo "✅ OpenAPI spec generated successfully!"
