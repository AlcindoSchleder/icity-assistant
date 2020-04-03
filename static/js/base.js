/*
    Theme Name: i-CityAssistant
    Author: Alcindo Schleder
    Author URL: https://icity.net.br
*/
var BaseEvents = function () {
    var ConfirmDialog = function (message) {
        if (confirm(message))
            return true;
        else
            return false;
    };
    return {
        //main function to initiate the module
        Init: function () {
        },
        Confirm: function (msg) {
            return ConfirmDialog(msg);
        }
    };
}();

$(document).ready(function () {
    BaseEvents.Init();
});
