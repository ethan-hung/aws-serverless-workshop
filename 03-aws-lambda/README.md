# AWS Lambda
1. AWS console -> Services -> Lambda
2. Click Create function
3. Input Function Name "aws-serverless-workshop-get" -> Choose Runtime "Python 3.7" -> Choose Execution role "Use an existing role" -> Choose Existing role "aws-lambda-service-role" -> Click "Create function"
![](../images/03-01.jpg)
4. Setting Lambda Environment
   * Environment variables
   * Tags 
![](../images/03-02.jpg)
5. Write your Code on Lambda
6. Click "Save"
7. 

3. Click Create Role
4. Choose "AWS Service" -> Click "Lambda" -> Click "Next:Permissions"
![](../images/02-01.jpg)
5. Select Policy "AWSLambdaVPCAccessExecutionRole" -> Click "Next:Tags"
![](../images/02-02.jpg)
6. Input Role name "aws-lambda-service-role" -> Click "Create role"