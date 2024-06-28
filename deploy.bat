@echo off

REM Define variables
set IMAGE_NAME=gcr.io/valeo-rnes/flask-app
set REGION=europe-west3
set SERVICE_NAME=flask-app

REM Submit the build to Google Cloud Build
gcloud builds submit --tag %IMAGE_NAME%

REM Deploy the application to Google Cloud Run
gcloud run deploy %SERVICE_NAME% --image %IMAGE_NAME% --region %REGION%
