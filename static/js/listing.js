
var pagerLinkAction = function(page){
    /* Click event for page links */
    $('.listing-pager').click(function(){
        var page = $(this).text();
        console.log('page number is initially:'+page);
        description = $('#description-select').val();
        location = $('#location-select').val();
        requestForJsonData(description,location,'refineSearch',page);
    });
};

/*  Function Dynamically builds page links on template based on page_count variable */
var buildPageLinks = function(page_count,record_count){
    console.log('building page links');
    console.log('page_count = '+page_count);
    console.log('record_count = '+record_count);
    if(0 < page_count){
        var page_links = $('#page_links');

        /*  clear contents of div */
        $('#page_links').html('');

        /*  rebuild page links */
        for(i=0;i<page_count;i++){
            var page_link = $('<a href="#" class="listing-pager">'+(i+1)+'</a>');
            page_links.append(page_link);

            /* Add divider between links */
            if((i+1)<page_count){
                page_links.append(' | ');
            }
        }
        pagerLinkAction();
    }
};

var populateTemplate = function(){

    // clear the SPINNER or previous searches
    $('#REST-data').html('');

    var page_count = 0;
    var record_count = 0;

    //  Parent div
    var restDataDiv = $('#REST-data');
    for(i=0;i<apiResponseArr.length;i++){
        console.log('id:'+apiResponseArr[i].id);
        console.log('title:'+apiResponseArr[i].title);
        console.log('description:'+apiResponseArr[i].description);
        console.log('genre:'+apiResponseArr[i].genre);
        console.log('location:'+apiResponseArr[i].location);
        console.log('profile_image_url:'+apiResponseArr[i].profile_image_url);
        console.log('bio_summary:'+apiResponseArr[i].bio_summary);
        var card = $('<div class="col-lg-3 col-md-6 col-xs-12 margin-top-1"><a href="/entertainers/profile/'+apiResponseArr[i].id+'"><div class="card h-100"><img class="card-img-top" src="'+apiResponseArr[i].profile_image_url+'" class="img-fluid center-block img-thumbnail" style="max-height:150px;" alt="'+apiResponseArr[i].profile_image_url+'" /><div class="card-body"><h4 class="card-title">'+apiResponseArr[i].title+'</h4><p class="card-text">'+apiResponseArr[i].bio_summary+'</p></div></div></a></div>');

        restDataDiv.append(card);

        if(0==i){
            page_count = apiResponseArr[i].page_count;
            record_count = apiResponseArr[i].record_count;


            buildPageLinks(page_count,record_count);
        }
    }
};

/* RETRIEVE SEARCH FILTER VALUES AND REQUEST JSON */
var refineSearch = function(menus){
    var description = 'all';
    var location = 'all';
    var page = 1
    /*  Build click event for the refine button */
    $('#refine-button').click(function(){
        description = $('#description-select').val();
        location = $('#location-select').val();
        requestForJsonData(description,location,'refineSearch',page);
    });
    pagerLinkAction(page);
};

/*  LOAD THE SELECT MENUS */
var loadMenus = function(menus){
    $.each(menus,function(index, value){
        if('description'==value){
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

    //  Display loading spinner
    $('#REST-data').html('<p id="spinner"><i class="fa fa-spinner fa-spin orange-spin"></i></p>');

    //  initially load all entertainers
    requestForJsonData('all','all','initLoad','all');
});

