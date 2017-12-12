var populateTemplate = function(){
    console.log('in populateTemplate');
    console.log('length of apiResponseArr is '+apiResponseArr.length);
            /*
        var i,j,arrayItem;
        for (i = 0; i < entertainerArr.length; ++i) {
            arrayItem = entertainerArr[i];
            for (j = 0; j < arrayItem.length; ++j) {
                console.log(arrayItem[j].title);
            }
        } */
    console.log('first title:'+apiResponseArr[0].title);
    for(i=0;i<apiResponseArr.length;i++){
        console.log('title:'+apiResponseArr[i].title);
        console.log('description:'+apiResponseArr[i].description);
        console.log('genre:'+apiResponseArr[i].genre);
        console.log('location:'+apiResponseArr[i].location);
    }
};

/* RETRIEVE SEARCH FILTER VALUES AND REQUEST JSON */
var refineSearch = function(menus){
    var description = 'all';
    var location = 'all';
    /*  Build click event for the refine button */
    $('#refine-button').click(function(){

        description = $('#description-select').val();
        location = $('#location-select').val();
        requestForJsonData(description,location,'refineSearch');
    });
};

/*  LOAD THE SELECT MENUS */
var loadMenus = function(menus){
    $.each(menus,function(index, value){
        if('description'==value){
            console.log('load the entertainer menu');
            var option = '';
            for(var i=0;i<descriptionArr.length;i++){
                if('All Entertainers' == descriptionArr[i]){
                    option += '<option value="all">'+descriptionArr[i]+'</option>';
                }else{
                    option += '<option value="'+descriptionArr[i]+'">'+descriptionArr[i]+'</option>';
                }
            }
            $('#description-select').append(option);
        }else if('location'==value){
            console.log('load the location menu');
            var option = '';
            for(var i=0;i<locationArr.length;i++){
                if('All Locations' == locationArr[i]){
                    option += '<option value="all">'+locationArr[i]+'</option>';
                }else {
                    option += '<option value="' + locationArr[i] + '">' + locationArr[i] + '</option>';
                }
            }
            $('#location-select').append(option);
        }
    })
};

/*  When the listing page loads */
$(document).ready(function(){
    console.log('page loaded');
    var menus = ['description','location'];

    loadMenus(menus);
    refineSearch(menus);
});

