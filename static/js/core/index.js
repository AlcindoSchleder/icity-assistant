/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
const IndexEvents = function () {
    const DocumentsEvents = function () {
        $('.icity-select').click(function() {
            $(this).toggleClass('active');
            const assistant = $('#pk_assistants').children("option:selected").val();
            if (assistant != '')
                $('.icity-button').removeClass('d-none');
            else
                $('.icity-button').addClass('d-none');
        });
        $('.btn-continue').click(() => {
            const pk = $('#pk_assistants').children("option:selected").val();
            const redirect = window.location.href + pk;
            redirectPost(redirect, {pk_assistants: pk});
        })
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
