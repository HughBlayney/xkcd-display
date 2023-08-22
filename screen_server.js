const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const fs = require('fs');
const chokidar = require('chokidar');
require('dotenv').config();

const SOCKET_URL = "wss://" + process.env.XKCD_SCREEN_SOCKET_URL || "default_url_here";
const IMAGE_PATH = process.env.XKCD_VIRTUAL_IMAGE_PATH || "default_path_here";

const app = express();
const screen_server = http.createServer(app);
const io = socketIo(screen_server);



app.set('view engine', 'ejs');  // Set the templating engine to ejs
app.set('views', __dirname);    // Set the views directory

app.get('/', (req, res) => {
    res.render('screen_client', {SOCKET_URL});  // Pass the SOCKET_URL variable to the client
});

app.get('/stream', (req, res) => {
    res.contentType('image/png');
    res.sendFile(__dirname + '/' + IMAGE_PATH);
});

io.on('connection', (socket) => {
    console.log('User connected');
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

const watcher = chokidar.watch(IMAGE_PATH);
watcher.on('change', (path) => {
    console.log(`Image updated: ${path}`);
    io.emit('image_updated');
});

screen_server.listen(3000, () => {
    console.log('Node server is running on port 3000');
});
