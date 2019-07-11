# AWS Lambda
1. AWS console -> Services -> Lambda
2. Click Create function
3. Input Function Name "aws-serverless-workshop-get" -> Choose Runtime "Python 3.7" -> Choose Execution role "Use an existing role" -> Choose Existing role "aws-lambda-service-role" -> Click "Create function"
![](../images/03-01.jpg)
4. Setting Lambda Environment
   * Environment variables
   * Tags
   * Execution role
   * Basic settings
   * Network
   * Debugging and handling
   * Concurrency
![](../images/03-02.jpg)
5. Write your Code on Lambda
6. Click "Save"
7. Click "Test" -> Create new test event -> Input Event name "demo" -> Create -> Click Test
![](../images/03-03.jpg)
8. Create another Lambda function name "aws-serverless-workshop-post"