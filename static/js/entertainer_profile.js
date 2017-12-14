$(document).ready(function(){
    /* Forward to login screen */
    $('#log-in-to-book').on('click',function(){
        var currentLocation = window.location;
        window.location.replace("/accounts/login/");
    });
});
