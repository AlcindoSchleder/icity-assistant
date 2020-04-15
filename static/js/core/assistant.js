/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const DocumentsEvents = function () {
        $(document).on('keydown', function(event) {
            const key = (event.keyCode ? event.keyCode : event.which);
            event.preventDefault();
            if (key == '27') {
                const href = window.location.href.replace('bot_assistant', 'bot');
                window.location.href = href;
            }
        });
        $('#sender-text').keypress(function(event) {
            const key = (event.keyCode ? event.keyCode : event.which);
            if (key == '13') {
                text = $('#sender-text').val();
                msgList = $('#list-messages')
                msgList.append(document.createElement('div'));
                $('#list-messages div:last').addClass('speech-bubble sender-bubble');
                $('#list-messages div:last').append(document.createTextNode(text));
                msgList.animate({
                    scrollTop: msgList.prop('scrollHeight')
                }, 1000);
                // send a message to Watson Assistant
            }
        });
        Pressed.Init(document.querySelector("#btn-act-microphone"));
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
