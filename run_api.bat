@echo off

::Check if Docker is running
docker info > nul 2>&1
if %errorlevel% neq 0 (
    echo Docker is not running.
    pause
    goto :EOF
)

:: Define the Docker image name and tag
set IMAGE_NAME=pred_loan
set TAG=v03
set CONTAINER_NAME=predv03

:: Check if the Docker image exists locally
docker inspect %IMAGE_NAME%:%TAG% > nul 2>&1
if %errorlevel% neq 0 (
    echo Image %IMAGE_NAME%:%TAG% does not exist locally. Building it...
    docker build -t %IMAGE_NAME%:%TAG% .
) else (
    echo Image %IMAGE_NAME%:%TAG% Found
)



:: Define the port mapping
set HOST_PORT=9696
set CONTAINER_PORT=9696

:: Run the Docker container
docker run --name %CONTAINER_NAME% -it --rm -p %HOST_PORT%:%CONTAINER_PORT% -d %IMAGE_NAME%:%TAG% > nul

echo Docker container started and ready to use
echo Launching the API...
timeout /t 3 > nul
start http://localhost:9696
echo API Started and Hosted on http://localhost:9696
echo Simply press a key to close it


:: Wait for a key press
pause

:: Stop and remove the Docker container 

docker stop %CONTAINER_NAME%


:: Wait for a key press and display a message
echo Containers stopped and removed. 
pause

