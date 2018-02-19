/*  REQUEST JSON FROM THE REST API */
var requestForJsonData = function(description,location,callingFunction, page){
    console.log('description is '+description);
    console.log('location is '+location);
    console.log('page is '+page);
    var host = window.location.hostname;

    // IF RUNNING ON LOCALHOST
    if('127.0.0.1'==host){
        var entertainerAPI = 'http://' + host + ':8000/entertainers/api/listings/?';
    }
    else{
        var entertainerAPI = 'https://' + host + '/entertainers/api/listings/?';
    }
    console.log('host is '+host);
    console.log('entertainerAPI is '+entertainerAPI);

    //  maybe ADD //format: "json" TO PARAMS????
    $.getJSON(entertainerAPI,{description: description,location: location, page: page}, function(){
        console.log('success');
    }).done(function( json ) {
        console.log('json is:');
        console.log( json );
        apiResponseArr = json;
        console.log('In requestForJsonData function, the length of apiResponseArr is '+apiResponseArr.length);
        // Check which function called the requestForJsonDat function
        if('refineSearch' == callingFunction || 'initLoad' == callingFunction){
            //  Call to populate the templates with the JSON data
            populateTemplate();
        }
    }).fail(function(jqxhr, textStatus, error){
        var err = textStatus + ", " + error;
        console.log( "Request Failed: " + err );
    });

};
