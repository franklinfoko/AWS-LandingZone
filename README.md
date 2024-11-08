# AWS-LandingZone-CloudFormation-template
Repository for CloudFormation template to create AWS Landing Zone with Control Tower

## To validate template
```
aws cloudformation validate-template --template-body file://landingZone.yml
```
## To create stack
```
aws cloudformation create-stack --stack-name MyStackName --template-body file://prerequisites.yml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=LoggingAccountName,ParameterValue=LoggingAccount ParameterKey=LoggingAccountEmail,ParameterValue=logging@example.com ParameterKey=SecurityAccountName,ParameterValue=SecurityAccount ParameterKey=SecurityAccountEmail,ParameterValue=security@example.com
```