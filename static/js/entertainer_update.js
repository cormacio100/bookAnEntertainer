/*  When the listing page loads */
$(document).ready(function(){
    /**
     * STYLE THE FORM
     *
     * Button is only element that is 12 cols across
     */
    $('.form-group').addClass('col-md-6');
    $('.form-group').addClass('col-sm-12');

    $('.form-group:contains(Update)').removeClass('col-md-6');
    $('.form-group:contains(Update)').removeClass('col-sm-12');
    $('.form-group:contains(Update)').addClass('col-12');
    $('.form-group:contains(Update)').addClass('margin-top-1');

});
