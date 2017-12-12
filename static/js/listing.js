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
    //  Placeholder
    //$('#REST-data').html("Loading...");

    //  Parent div
    var restDataDiv = $('#REST-data');
    //var cardArr = [];

    for(i=0;i<apiResponseArr.length;i++){
        console.log('id:'+apiResponseArr[i].id);
        console.log('title:'+apiResponseArr[i].title);
        console.log('description:'+apiResponseArr[i].description);
        console.log('genre:'+apiResponseArr[i].genre);
        console.log('location:'+apiResponseArr[i].location);
        console.log('profile_image_url:'+apiResponseArr[i].profile_image_url);
        console.log('bio_summary:'+apiResponseArr[i].bio_summary);
        var card = $('<div class="col-3 ent-listing"><div class="card"><img class="card-img-top" src="'+apiResponseArr[i].profile_image_url+'" class="img-fluid center-block img-thumbnail" style="max-height:150px;" alt="Card image cap" /><div class="card-body"><h4 class="card-title">'+apiResponseArr[i].title+'</h4><p class="card-text">'+apiResponseArr[i].bio_summary+'</p></div><div class="card-footer"><small class="text-muted"><a href="/entertainers/profile/'+apiResponseArr[i].id+'">...Read More</a></small></div></div></div>');

        restDataDiv.append(card);
    }

    /*
<div class="col-3 ent-listing"><div class="card"><img class="card-img-top" src="{{ entertainer.profile_image.url }}" class="img-fluid center-block img-thumbnail" style="max-height:150px;" alt="Card image cap"><div class="card-body"><h4 class="card-title">{{ entertainer.title }}</h4><p class="card-text">{{ entertainer.bio_summary }}</p></div><div class="card-footer"><small class="text-muted"><a href="{% url 'entertainers:profile' entertainer.id %}">...Read More</a></small></div></div></div>*/


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

