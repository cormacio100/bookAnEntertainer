/*  When the listing page loads */
$(document).ready(function(){
    /**
     * STYLE THE FORM
     *
     * Button is only element that is 12 cols across
     */
    $('.form-group').addClass('col-md-6');
    $('.form-group').addClass('col-sm-12');

    $('.form-group:contains(Register)').removeClass('col-md-6');
    $('.form-group:contains(Register)').removeClass('col-sm-12');
    $('.form-group:contains(Register)').addClass('col-12');
    $('.form-group:contains(Register)').addClass('margin-top-1');

});
