/**
 * Click event for page links
 */
var pagerClick = function(pageClicked){
    var description = $('#description-select').val();
    var location = $('#location-select').val();
    var page = pageClicked;
    requestForJsonData(description,location,'refineSearch',page);
}

var populateTemplate = function(){
    // clear the SPINNER or previous searches
    $('#REST-data').html('');

    var page_count = 0;
    var record_count = 0;

    //  Parent div
    var restDataDiv = $('#REST-data');
    var counter = 0;

    for(i=0;i<apiResponseArr.length;i++){
        var card = $('<div class="col-lg-3 col-md-6 col-xs-12 margin-top-1"><a href="/entertainers/profile/'+apiResponseArr[i].id+'"><div class="card h-100"><img class="card-img-top" src="'+apiResponseArr[i].profile_image_url+'" class="img-fluid center-block img-thumbnail" style="max-height:150px;" alt="'+apiResponseArr[i].profile_image_url+'" /><div class="card-body"><h4 class="card-title">'+apiResponseArr[i].title+'</h4><p class="card-text">'+apiResponseArr[i].bio_summary+'</p></div></div></a></div>');
        restDataDiv.append(card);

        /**
         *  Build the PAGER LINKS
         *  Only need to retrieve the page and record count from first record as all contain the same
         */
        if(0==i){
            page_count = apiResponseArr[i].page_count;
            record_count = apiResponseArr[i].record_count;


            // CLEAR THE page_links DIV before appending the pages to it
            var link = '';
            $('#page_links').html('')

            for(j=0; j < page_count; j++){
                link = $('<a href="#" class="listing-pager">'+(j+1)+'</a>');
                $('#page_links').append(link);

                /* Add divider between links */
                if((j+1)<page_count){
                    $('#page_links').append(' | ');
                }
            }
            //  Create click action for the links
            $('.listing-pager').click(function(){
                var page = $(this).text();
                pagerClick(page)
            });
        }

        counter++;
    }
    console.log('page_count = '+page_count);
    console.log('record_count = '+record_count);
};

/* RETRIEVE SEARCH FILTER VALUES AND REQUEST JSON */
var refineSearch = function(menus){
    var description = 'all';
    var location = 'all';
    var page = '1'
    /*  Build click event for the refine button */
    $('#refine-button').click(function(){
        description = $('#description-select').val();
        location = $('#location-select').val();
        requestForJsonData(description,location,'refineSearch',page);
    });
    $('.listing-pager').click(function(){
        var page = $(this).text();
        pagerClick(page)
    });
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
    var menus = ['description','location'];

    loadMenus(menus);
    refineSearch(menus);

    //  Display loading spinner
    $('#REST-data').html('<p id="spinner"><i class="fa fa-spinner fa-spin orange-spin"></i></p>');

    //  initially load all entertainers on the first page of 8 records
    requestForJsonData('all','all','initLoad',1);
});

