/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const DocumentsEvents = function () {
        $(document).on('keydown', function(event){
            const key = (event.keyCode ? event.keyCode : event.which);
            const proto = window.location.protocol;
            const port = window.location.port;
            const host = window.location.hostname;
            if (key == '27') {
                const href = proto + '//' + host + ':' + (((port == 80) || (port == 443)) ? '' : port);
                redirectPost(href, {});
            }
            if (key == '13') {
                const href = window.location.href.replace('bot', 'bot_assistant');
                console.log('call ' + href + ' with post')
                const pka = $('#pk').html();
                const dsca = $('#dsc').html();
                redirectPost(href, {pk: pka, dsc: dsca});
            }
        });
    };
    const redirectPost = function(location, args) {
        let fields = '';
        $.each(args, function(key, value) {
            fields += '<input type="hidden" name="'+key+'" value="'+value+'">\r';
        });
        $('#form-temp').attr('action', location);
        if (fields != '')
            $('#form-temp.fields').append(fields);
        $('#form-temp').submit();
    }
    return {
        //main function to initiate the module
        Init: function () {
            DocumentsEvents();
        }
    };
}();

$(document).ready(function () {
    //normalize window.URL
    IndexEvents.Init()
});
