const jwt = require('jsonwebtoken');
const JWT_EXPIRATION_TIME = '5m';


exports.handler = async (event) => {
    // TODO implement
    console.log('login');
    console.log(event);
    var username = event.username;
    var password = event.password;
    
    // Only check if user is test and password is 1234 for now
    // Can connect to a DB and check if user is registered in it
    if (username == 'test' && password == '1234'){
        // Issue JWT
        const token = jwt.sign({ username }, process.env.JWT_SECRET, { expiresIn: JWT_EXPIRATION_TIME });
        console.log(`JWT issued: ${token}`);
        const response = { // Success response
            statusCode: 200,
            headers: {
                'Access-Control-Allow-Origin': '*',
            },
            body: JSON.stringify({
                 token,
            }),
         };
         return response;
    }
    const response = {
        statusCode: 401,
        body: JSON.stringify('Access Denied'),
        };
    return response;
};
