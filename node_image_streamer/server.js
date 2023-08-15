const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const fs = require('fs');
const chokidar = require('chokidar');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const IMAGE_PATH = "static/display.png";

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
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

// Use chokidar to watch the image file for changes
const watcher = chokidar.watch(IMAGE_PATH);

watcher.on('change', (path) => {
    console.log(`Image updated: ${path}`);
    io.emit('image_updated');
});

server.listen(3000, () => {
    console.log('Node server is running on port 3000');
});
