/*  REQUEST JSON FROM THE REST API */
var requestForJsonData = function(description,location,callingFunction){
    console.log('description is '+description);
    console.log('location is '+location);
    var host = window.location.hostname;

    // IF RUNNING ON LOCALHOST
    // var entertainerAPI = 'http://' + host + ':8000/entertainers/api/listings/?';
    // ELSE
    var entertainerAPI = 'https://' + host + '/entertainers/api/listings/?';
    console.log('entertainerAPI is '+entertainerAPI);

    //  maybe ADD //format: "json" TO PARAMS????
    $.getJSON(entertainerAPI,{description: description,location: location,}, function(){
        console.log('success');
    }).done(function( json ) {
        console.log( json );
        apiResponseArr = json;
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
