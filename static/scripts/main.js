// submit post on submit

$(document).ready(function() {
    $('#id_car_make').change('car_make', function(event){
        event.preventDefault();
        console.log("appointment form submitted!")  // sanity check
        create_appointment();
    });
});

// AJAX for posting
function create_appointment() {
    console.log("create appointment is working!") // sanity check
    $.ajax({
        url : "/cars/model/?make=" + $('#id_car_make').val(), // the endpoint
        type : "GET", // http method

        // handle a successful response
        success : function(json) {
//            $('#id_car_make').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            // Log each key in the response data
            var options = '<option value="">--------&nbsp;</option>';
            $('#id_car_model').html(options)
            $.each( json, function(key, value) {
                options += '<option value="' + value + '">' + value + '</option>';
                $('#id_car_model').html(options)
                console.log( key + " : " + value );
            });
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};