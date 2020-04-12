/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const DocumentsEvents = function () {
        $(document).keypress(function(event){
            const key = (event.keyCode ? event.keyCode : event.which);
            if(key == '13') {
                alert('Abre o chat bot')
            }
        });
    };
    const redirectPost = function(location, args) {
        let fields = '';
        $.each( args, function( key, value ) {
            fields += '<input type="hidden" name="'+key+'" value="'+value+'">\r';
        });
        $('#form-temp').attr('action', location);
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
