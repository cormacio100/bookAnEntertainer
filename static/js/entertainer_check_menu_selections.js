/**
 * Populate relevant DOM menus based on DESCRIPTION option chosen
 */

/**
 * Max price should NOT be less than Min price
 */
checkPrice = function(){

    $('#id_min_price').on('change',function(){
        var min = parseInt($('#id_min_price').val(),10);
        var max = parseInt($('#id_max_price').val(),10);
        if(max < min){
            $('#id_max_price').val(min);
        }
    });
};

/**
 * "Gig length from" must be less than or equal to "Gig length to" options
 */
checkGigLength = function(){
    $('#id_gig_length_from').on('change',function(){
        var from = parseInt($('#id_gig_length_from').val(),10);
        var to = parseInt($('#id_gig_length_to').val(),10);

        if(to < from){
            $('#id_gig_length_to').val(from);
        }
    });
};

/**
 * Check the value of the Description menu
 * -    If Comedian, Genre and Music options will auto populate
 */
checkDescription = function(){
    $('#id_description').on('change',function(){
        var val = $('#id_description').val();
        if('Comedian'==val){
            $('#id_genre').val('Other');
            $('#id_music_3').prop('checked', true);
            $('#id_influences').val('Comedy and Life');
        }else{
            $('#id_music_3').prop('checked', false);
            $('#id_influences').val('All Genres and decades.');
        }
    });
};

/**
 * CHECK Selections as they can determine values in other menus
 */
checkMenus = function(){
    checkDescription();
    checkGigLength();
    checkPrice();
};