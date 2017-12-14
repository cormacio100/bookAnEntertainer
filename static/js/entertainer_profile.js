/*  When the listing page loads */
$(document).ready(function(){
    $('#log-in-to-book').on('click',function(){
        console.log('logging in');
        var currentLocation = window.location;
        console.log('current location:'+currentLocation);
        window.location.replace("/accounts/login/");
    });
});
