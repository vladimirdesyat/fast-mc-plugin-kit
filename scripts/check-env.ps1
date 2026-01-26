$tools = @("java", "mvn", "python", "cookiecutter")

foreach ($tool in $tools) {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
        Write-Host "Missing dependency: $tool" -ForegroundColor Red
        exit 1
    }
}

Write-Host "Environment OK" -ForegroundColor Green