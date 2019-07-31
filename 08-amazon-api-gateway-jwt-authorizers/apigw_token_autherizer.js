const jwt = require('jsonwebtoken');


// A simple token-based authorizer example to demonstrate how to use an authorization token 
// to allow or deny a request.
exports.handler =  function(event, context, callback) {
    var token = event.authorizationToken;
    console.log(token);
    var tokencase = '';
    // Verify JWT
    try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    console.log(JSON.stringify(decoded));
    const user = decoded.username;
    console.log(user);
    if (user == "test"){
        // for testing purpose, only allow when the username is 
        tokencase = 'allow';
    } else {
        tokencase = 'deny';
    }    
    } catch (e) {
        console.log(e);
    }

    switch (tokencase) {
        case 'allow':
            console.log("allow");
            callback(null, generatePolicy('user', 'Allow', event.methodArn));
            break;
        case 'deny':
            console.log("deny");
            callback(null, generatePolicy('user', 'Deny', event.methodArn));
            break;
        case 'unauthorized':
            console.log("unauthorized");
            callback("Unauthorized");   // Return a 401 Unauthorized response
            break;
        default:
            callback("Error: Invalid token"); // Return a 500 Invalid token response
    }
};

// Help function to generate an IAM policy
var generatePolicy = function(principalId, effect, resource) {
    var authResponse = {};
    
    authResponse.principalId = principalId;
    if (effect && resource) {
        var policyDocument = {};
        policyDocument.Version = '2012-10-17'; 
        policyDocument.Statement = [];
        var statementOne = {};
        statementOne.Action = 'execute-api:Invoke'; 
        statementOne.Effect = effect;
        statementOne.Resource = resource;
        policyDocument.Statement[0] = statementOne;
        authResponse.policyDocument = policyDocument;
    }
    
    // Optional output with custom properties of the String, Number or Boolean type.
    authResponse.context = {
        "stringKey": "stringval",
        "numberKey": 123,
        "booleanKey": true
    };
    return authResponse;
}