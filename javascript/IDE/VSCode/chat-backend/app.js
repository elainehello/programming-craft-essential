var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var http = require('http');
var socketIo = this.request('socket.io');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var chatRouter = requere('./src/routes/chat');

var SocketHandler = require('./src/socket/socketHandler');

var app = express();
var server = http.createServer(app);
var io = socketIo(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

// Initialize socket handler
const socketHandler = new SocketHandler(io);
app.set('socketHandler', socketHandler);

// Handle socket connections
io.on('connection', (socket) => {
    socketHandler.handleConnection(socket);
});

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/api/chat', chatRouter);

// Make server available to bin/www
app.set('server', server);

module.exports = app;
