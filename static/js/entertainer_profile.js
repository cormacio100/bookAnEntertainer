$(document).ready(function(){
    /* Forward to login screen */
    $('#log-in-to-book').on('click',function(){
        var currentLocation = window.location;
        window.location.replace("/accounts/login/");
    });
    //  change the paypal button to Book us instead of Buy Now
    $("div#paypal_form_div > form > input[name='submit']").attr("src","https://s3-eu-west-1.amazonaws.com/bookanentertainer4/static/img/book_now_orange.png");
    console.log('paypal button image switched');

});
