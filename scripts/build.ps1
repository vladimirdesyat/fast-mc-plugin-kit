$ROOT_DIR     = Resolve-Path "$PSScriptRoot\.."
$PROJECTS_DIR = "$ROOT_DIR\projects"
$PLUGINS_DIR  = "$ROOT_DIR\plugins"

Write-Host "=== Maven Plugin Builder ===" -ForegroundColor Cyan

if (-not (Test-Path $PROJECTS_DIR)) {
    Write-Error "Projects directory not found: $PROJECTS_DIR"
    exit 1
}

New-Item -ItemType Directory -Force -Path $PLUGINS_DIR | Out-Null

Get-ChildItem $PROJECTS_DIR -Directory | ForEach-Object {

    $PROJECT_PATH = $_.FullName
    $PROJECT_NAME = $_.Name
    $TARGET_DIR   = "$PROJECT_PATH\target"

    Write-Host "`n>>> Processing $PROJECT_NAME" -ForegroundColor Yellow

    # Checking pom.xml
    if (-not (Test-Path "$PROJECT_PATH\pom.xml")) {
        Write-Warning "Skipping: pom.xml not found"
        return
    }

    # Finding jar
    $JAR = Get-ChildItem "$TARGET_DIR\*.jar" -ErrorAction SilentlyContinue |
           Where-Object { $_.Name -notmatch "original" } |
           Select-Object -First 1

    if (-not $JAR) {
        Write-Host "No JAR found. Building..." -ForegroundColor Gray

        Push-Location $PROJECT_PATH
        mvn clean package -q
        Pop-Location

        $JAR = Get-ChildItem "$TARGET_DIR\*.jar" |
               Where-Object { $_.Name -notmatch "original" } |
               Select-Object -First 1

        if (-not $JAR) {
            Write-Error "Build failed: no JAR produced"
            return
        }
    } else {
        Write-Host "JAR already exists. Skipping build." -ForegroundColor DarkGray
    }

    $DEST = "$PLUGINS_DIR\$PROJECT_NAME.jar"
    Copy-Item $JAR.FullName $DEST -Force

    Write-Host "Copied -> plugins/$PROJECT_NAME.jar" -ForegroundColor Green
}

Write-Host "`nDone." -ForegroundColor Cyan