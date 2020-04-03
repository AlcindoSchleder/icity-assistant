/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const DocumentsEvents = function () {
        $('#sender-text').keypress(function(event){
            const key = (event.keyCode ? event.keyCode : event.which);
            if(key == '13') {
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
        // $('.btn-act-microphone').click(async (e) => {
        // Open Microphone and save into file for send to Watson Assistant
        // if ((WebAudio === undefined) || (WebAudio.checkRecord() === undefined))
        //     return false
        // if (WebAudio.checkRecord()) {
        //     WebAudio.startRecord();
        // } else {
        //     await WebAudio.stopRecord();
        //     WebAudio.playAudio();
        // }
        // });
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
