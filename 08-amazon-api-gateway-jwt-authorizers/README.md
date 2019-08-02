# Amazon API Gateway JWT Authorizers

There are two types of Lambda authorizers:
1. token-based Lambda authorizer: For JSON Web Token or OAuth token
2. request parameter-based Lambda authorizer: For WebSocket APIs

## Lambda Authorizers workflow
![](../images/08-01.png)

## Tutorial
![](../images/08-03.jpg)
1. Create "Autherizer" Lambda Function 
* Function Name "apigw_token_authorizer"
* Runtime "Node.js 10.x"
* Upload Lambda zip "apigw_token_authorizer.zip"
* Input Environment Variables "JWT_SECRET" "IMP"
![](../images/08-02.jpg)
2. Create "Login" Lambda Function
* Function Name "jwt_login"
* Runtime "Node.js 10.x"
* Upload Lambda zip "jwt_login_test.zip"
* Input Environment Variables "JWT_SECRET" "IMP"
3. Setting Amazon API Gateway Login
* Create Resource
* Path Name "login"
* Click "OK"
* Create Method
* Choose "POST"
* Input Lambda Function "jwt_login"
* Click "Save"
4. Setting Amazon API Gateway Authorizer
* Click "Authorizers"
* Click "Create New Authorizer"
* Input Name "api_authorizer"
* Input Lambda Function "apigw_token_authorizer"
* Input Token Source "token"
* Click "Create"
![](../images/08-04.jpg)
* Click API Name
* Click Method Request
![](../images/08-05.jpg)
* Choose Authorization "api_authorizer"
![](../images/08-06.jpg)
5. Deploy API
6. Testing Login API
* Open Postman
* Create New Request
* Select HTTP POST
* Input URL
* Input Body
```json
{
	"username": "test",
	"password": "1234"
}
```
* Click Send
* You can get the API Result
```json
{
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*"
    },
    "body": "{\"token\":\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJpYXQiOjE1NjQ3MjUyNTIsImV4cCI6MTU2NDcyNTU1Mn0.q8giND7oQW7n9zZdQNDX8zzEsGwsW0Fzufb_bf-Yciw\"}"
}
```
* Copy Login Result body token
![](../images/08-07.jpg)
7. Testing currect Token Authorizer API
* Create New Request
* Select HTTP GET
* Input URL
* Input Header token
* Click Send
![](../images/08-08.jpg)
8. Testing Error Token Authorizer API
* Input error Token
* Click Send
![](../images/08-09.jpg)