# Alexa Python Skill Template

This template is a fork of the [how to skill template](https://github.com/alexa/skill-sample-python-howto) tested in es-MX locale, with a script which improves workflow of publishing and testing the skill and with a working demo of a request being made to a third party service.

Here is a [link](https://github.com/alexa/skill-sample-python-howto/tree/master/instructions) to more detailed instructions on setting up the skill, but basically:

Be sure to create and work your items in the same region, you can see the region you are working as a get parameter in the aws console links: `https://console.aws.amazon.com/lambda/home?region=us-east-1#/`.
During the `aws configure` you will use this region in this case `us-east-1`
### 11 easy steps to run and test this template:
1. [Create an AWS account](https://console.aws.amazon.com/)
2. [Create an AWS IAM group with admin permissions and user to get aws-cli credentials](https://console.aws.amazon.com/iam/home)
3. [Create an Amazon Developer account](https://developer.amazon.com/)
4. [Create the skill, set an invocation name (make it conversational) and follow the steps in order to build the model](https://developer.amazon.com/alexa/console/ask)
5. [Create an AWS Lambda function to support the service for the skill:](https://console.aws.amazon.com/lambda/home)
    - From 0
    - Python 3.6
    - Role from template
    - Permission for simple microservices
> There are some templates or blueprints in there if you search for `alexa`, but this is what worked for me because this way I am able to work on my editor instead of the amazon lambda editor
6. Change `<FUNCTION_NAME>` in `publish.sh`
7. In the `Endpoint` tab in the [developer console](https://developer.amazon.com/alexa/console/ask) link your skill with your service by providing the ARN of your lambda function.
> At this point you should be able to see your skill listed as a dev skill under the `Skills > Your Skills > Dev Skills` menu in the [Alexa Console](https://alexa.amazon.com/spa/index.html#skills/your-skills/?ref-suffix=ysa_gw).
8. After succesfully setting an invocation name, saving and building the model and saving the endpoint, head over to the test tab so we can interact with alexa in the developers console.
9. Talk or write: `alexa <activate_word> <invocation_name>` in where `<activate_word>` can be replaced for words like: `open`, `abrir`, `preguntar` and *others*. 
10. Copy the json input that your call produces and paste it on the lambda console under the `Configure test event > New test event` option this way, you have a way to easily test and debug your function for this specific intent.
11. Share your skill and any improvements to this template :))
