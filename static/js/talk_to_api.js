/*  REQUEST JSON FROM THE REST API */
var requestForJsonData = function(description,location,callingFunction){
    console.log('description is '+description);
    console.log('location is '+location);
    var host = window.location.hostname;
    var entertainerAPI = 'http://' + host + ':8000/entertainers/api/listings/?';
    console.log('entertainerAPI is '+entertainerAPI);

    $.getJSON(entertainerAPI,{
        description: description,
        location: location,
        //format: "json"
    }, function(){
        console.log('success');

    }).done(function( json ) {
        console.log( "JSON Data: ");
        console.log( json );
        apiResponseArr = json;
        console.log('length of apiResponseArr is '+apiResponseArr.length);

        // Check which function called the requestForJsonDat function
        if('refineSearch' == callingFunction){
            //  Call to populate the templates with the JSON data
            populateTemplate();
        }
    }).fail(function(jqxhr, textStatus, error){
        var err = textStatus + ", " + error;
        console.log( "Request Failed: " + err );
    });


        /*
        .fail(function( jqxhr, textStatus, error ) {
        var err = textStatus + ", " + error;
        console.log( "Request Failed: " + err );
    });*/
};
