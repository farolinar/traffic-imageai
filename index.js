
const path = require('path');
const express = require('express');
const WebSocket = require('ws');
const app = express();

const WS_PORT = process.env.WS_PORT || 3001;
const HTTP_PORT = process.env.HTTP_PORT || 3000;

const wsServer = new WebSocket.Server({ port: WS_PORT }, () => console.log(`WS server is listening at ws://localhost:${WS_PORT}`));

// array of connected websocket clients
let connectedClients = [];

// wsServer.on('connection', (ws, req) => {
//     console.log('Connected');
//     // add new connected client
//     connectedClients.push(ws);
//     // listen for messages from the streamer, the clients will not send anything so we don't need to filter
//     ws.on('message', data => {
//         // send the base64 encoded frame to each connected ws
//         connectedClients.forEach((ws, i) => {
//             if (ws.readyState === ws.OPEN) { // check if it is still connected
//                 ws.send(data); // send
//             } else { // if it's not connected remove from the array of connected ws
//                 connectedClients.splice(i, 1);
//             }
//         });
//     });
// });


// var http = require( "http" );
// var http_server = http.createServer( app ).listen( 3003 );
// var http_io = require( "socket.io" )( http_server );

// http_io.on( "connection", function( httpsocket ) {
//     httpsocket.on( 'python-message', function( fromPython ) {
//         // httpsocket.broadcast.emit( 'message', fromPython );
//         console.log(fromPython);
//     });
// });
// var net = require('net');

// var client = new net.Socket();
// client.connect(8484, '127.0.0.1', function() {
//     console.log('Connected');
//     client.write('Hello, server! Love, Client.');
// });

// client.on('data', function(data) {
//     console.log('Received: ' + data);
//     // client.destroy(); // kill client after server's response
// });

// static stuff
app.use(express.static(__dirname + '/static'));

// HTTP stuff
app.get('/', (req, res) => res.sendFile(path.resolve(__dirname, './home.html')));
app.get('/client', (req, res) => res.sendFile(path.resolve(__dirname, './client.html')));
app.get('/streamer', (req, res) => res.sendFile(path.resolve(__dirname, './streamer.html')));
app.listen(HTTP_PORT, () => console.log(`HTTP server listening at http://localhost:${HTTP_PORT}`));