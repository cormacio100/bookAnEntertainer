var loadMenus = function(menus){
    $.each(menus,function(index, value){
        if('entertainer'==value){
            console.log('load the entertainer menu');
            var option = '';
            for(var i=0;i<entertainerArr.length;i++){
                option += '<option value="'+entertainerArr[i]+'">'+entertainerArr[i]+'</option>';
            }
            $('#entertainer-select').append(option);
        }else if('location'==value){
            console.log('load the location menu');
            var option = '';
            for(var i=0;i<locationArr.length;i++){
                option += '<option value="'+locationArr[i]+'">'+locationArr[i]+'</option>';
            }
            $('#location-select').append(option);
        }
    })
};
/*  When the listing page loads */
$(document).ready(function(){
    console.log('page loaded');
    var menus = ['entertainer','location'];

    loadMenus(menus);

    /*
    *   Need to put in OnChange event for the menus that detects what was selected
    *
    * */
});

