
# Create reports directory if it does not exist
New-Item -ItemType Directory -Force -Path "reports" | Out-Null

# Run tests in parallel and generate reports
pytest -n auto tests `
    --junitxml=reports/junit.xml `
    --html=reports/report.html `
    --self-contained-html

