cd lambda 
rm lambda.zip 
rm -rf skill_env
python --version #this is to verify im running that im running the python environment that i want
pip install -r py/requirements.txt -t skill_env
cp -r py/* skill_env/
cd skill_env
zip -X -r ../lambda.zip *
cd .. 
aws lambda update-function-code --profile <AWS_CREDENTIALS_PROFILE> --function-name <AWS_LAMBDA_FUNCTION_NAME> --zip-file fileb://lambda.zip

