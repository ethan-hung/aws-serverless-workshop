# AWS IAM Role
1. AWS console -> Services -> IAM
2. Click Roles
3. Click Create Role
4. Choose "AWS Service" -> Click "Lambda" -> Click "Next:Permissions"
![](../images/02-01.jpg)
5. Select Policy "AWSLambdaVPCAccessExecutionRole" -> Click "Next:Tags"
![](../images/02-02.jpg)
6. Input Role name "aws-lambda-service-role" -> Click "Create role"