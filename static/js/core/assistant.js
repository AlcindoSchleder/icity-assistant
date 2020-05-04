/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const user = $('#user').val()
    const assistant_id = $('#assistant_id').val()
    const terminalID = $('#terminal_id').val()
    const socketURL = 'ws://' + window.location.host + '/ws/assistant/' +
                    assistant_id + '/' + terminalID;

    const DocumentsEvents = function () {
        $(document).on('keydown', function(event) {
            const key = (event.keyCode ? event.keyCode : event.which);
            if (key == '27') {
                event.preventDefault();
                const href = window.location.href.replace('assistant', 'bot');
                window.location.href = href;
            }
        });
        $('#sender-text').keypress(function(event) {
            const key = (event.keyCode ? event.keyCode : event.which);
            if (key == '13') {
                text = $('#sender-text').val();
                writeMessage('sender-bubble', text);
                // detect language and translate if necessary
                sendMessages('text_bot', text)
                // send a message to Watson Assistant
            }
        });
        Pressed.Init(document.querySelector("#btn-act-microphone"));
    };
    const startWebSocket = function () {
        const assistantSocket = new WebSocket(socketURL);
        assistantSocket.onmessage = onMessage
        assistantSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };
    };
    const onMessage = function(e) {
        const data = JSON.parse(e.data);
        writeMessage('receiver-bubble', data.message)
    };
    const writeMessage = function (sender, message) {
        msgList = $('#list-messages')
        msgList.append(document.createElement('div'));
        $('#list-messages div:last').addClass('speech-bubble ' + sender);
        $('#list-messages div:last').append(document.createTextNode(message));
        msgList.animate({
            scrollTop: msgList.prop('scrollHeight')
        }, 1000);
    };
    const sendMessages = function (command, message) {
        console.log('Enviando/Recebendo dados de: ', display_id, sockets);
        sockets[display_id].send(JSON.stringify({
            'command': command,
            'user': user,
            'assistant_id': assistant_id,
            'terminal_id': terminalID,
            'message': message
        }));
    };

    return {
        //main function to initiate the module
        Init: function () {
            DocumentsEvents();
        }
    };
}();

$(document).ready(function () {
    //normalize window.URL
    window.URL || (window.URL = window.webkitURL || window.msURL || window.oURL);
    IndexEvents.Init()
});
