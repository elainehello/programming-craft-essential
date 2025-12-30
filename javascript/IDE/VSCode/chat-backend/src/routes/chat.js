const express = require('express');
const router = express.Router();


/* GET chat rooms listing */
router.get('/rooms', function(req, res, next) {
    // This will be populated by socket handler
    const socketHandler = req.app.get('socketHandler');
    const rooms = socketHandler ? socketHandler.getRoomList() : [];

    res.json({
        success: true,
        rooms
    });
});

/* Post create new room */
router.post('/rooms', function(req, res, next) {
    const { roomName } = req.body;

    if (!roomName) {
        return res.status(400).json({
            success: false,
            error: 'Room name is required'
        });
    }

    res.json({
        success: true,
        roomId: roomName.toLowerCase().replace(/\s+/g, '-'),
        message: 'Room created successfully'
    });
});

module.exports = router;
