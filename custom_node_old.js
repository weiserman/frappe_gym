// content of custom_node.js
const http = require('http')
const port = 4200

var fs = require('fs');
var path = require('path');
var redis = require('redis');


const requestHandler = (request, response) => {
    console.log(request.url)
    response.end('Hello this is Warrens Node.js Server!')
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {
    if (err) {
        return console.log('something bad happened', err)
    }

    console.log(`server is listening on ${port}`)
})