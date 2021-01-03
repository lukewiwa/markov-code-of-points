#!/bin/bash
set -e

npm install --prefix="$PROJECT_DIR"/markov-code-of-points-cdk/
cd "$PROJECT_DIR"/src/ && poetry install

cd "$PROJECT_DIR"

exec "$@"
