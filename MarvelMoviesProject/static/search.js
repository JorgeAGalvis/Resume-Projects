$(document).ready(function() {

    // Redirect to movie view 
    $( ".movie-div" ).click(function() {
        let movieId = $( this ).data("id")
        var redirectTo = "/view/" + movieId 
        $(location).attr('href',redirectTo)
    })

})

