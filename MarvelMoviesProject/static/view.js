$(document).ready(function() {

    // Redirect to movie view 
    $( ".suggestion-div" ).click(function() {
        let movieId = $( this ).data("id")
        var redirectTo = "/view/" + movieId 
        $(location).attr('href',redirectTo)
    })

    // Redirect when the user hits director 
    $( ".view-director-div" ).click(function() {
        let director = $( this ).html()
        var redirectTo = `/search?search-input=${director}`
        $(location).attr('href',redirectTo)
    })


    // Redirect when the user hits cast 
    $( ".view-cast-div" ).click(function() {
        let star = $( this ).html()
        var redirectTo = `/search?search-input=${star}`
        $(location).attr('href',redirectTo)
    })


    // Redirect when the user hits genre 
    $( ".view-genre-div" ).click(function() {
        let genre = $( this ).html()
        var redirectTo = `/search?search-input=${genre}`
        $(location).attr('href',redirectTo)
    })

    // Redirect when user hit edit 
    $('#view-edit-button').click(function(event) {
        let movieId = movieJSON["id"]
        var redirectTo = "/edit/" + movieId 
        $(location).attr('href',redirectTo)
    })


})