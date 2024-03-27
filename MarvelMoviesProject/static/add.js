function showDirectorsInput() {
    var numDirectors = $("#num-directors").val()
    var directorsInputsContainer = $("#directors-inputs")

    directorsInputsContainer.empty()

    for (let i = 0; i < numDirectors; i++) {
        var inputGroup = $("<div>").addClass("input-group mb-2")

        var input = $("<input>").attr({
            type: "text",
            class: "form-control",
            id: `director-${i}`, 
            placeholder: "Director " + (i+1)
        });

        inputGroup.append(input)
        directorsInputsContainer.append(inputGroup)
    }

    if (numDirectors > 0) {
        directorsInputsContainer.show()
    } else {
        directorsInputsContainer.hide()
    }

    return numDirectors
}


function showStarsInput() {
    var numStars = $("#num-stars").val()
    var starsInputsContainer = $("#stars-inputs")

    starsInputsContainer.empty()

    for (var i = 0; i < numStars; i++) {
        var inputGroup = $("<div>").addClass("input-group mb-2")

        var input = $("<input>").attr({
            type: "text",
            class: "form-control",
            id:`star-${i}`,
            placeholder: "Star " + (i+1)
        })

        inputGroup.append(input)
        starsInputsContainer.append(inputGroup)
    }

    if (numStars > 0) {
        starsInputsContainer.show()
    } else {
        starsInputsContainer.hide()
    }

    return numStars
}

function showSimilarInput(similarMovies) {
    var numSimilar = $("#num-similar").val()
    var similarInputsContainer = $("#similar-inputs")

    similarInputsContainer.empty()

    for (var i = 0; i < numSimilar; i++) {
        var inputGroup = $("<div>").addClass("input-group mb-2")

        var select = $("<select>").attr({
            class: "form-control",
            id: `similar-${i}`,
            placeholder: "Similar " + (i + 1)
        });

        $.each(similarMovies, function (index, value) {
            // in value, index + 1 to grab the right id 
            var option = $(`<option value="${index+1}">${value}</option>`)
            select.append(option)
        });

        inputGroup.append(select)
        similarInputsContainer.append(inputGroup)
    }

    if (numSimilar > 0) {
        similarInputsContainer.show()
    } else {
        similarInputsContainer.hide()
    }

    return numSimilar;
}

function showGenresInput() {
    var numGenres = $("#num-genres").val()
    var genresInputsContainer = $("#genres-inputs")

    genresInputsContainer.empty()

    for (var i = 0; i < numGenres; i++) {
        var inputGroup = $("<div>").addClass("input-group mb-2")

        var input = $("<input>").attr({
            type: "text",
            class: "form-control",
            id:`genre-${i}`,
            placeholder: "Genre " + (i+1)
        })

        inputGroup.append(input)
        genresInputsContainer.append(inputGroup)
    }

    if (numGenres > 0) {
        genresInputsContainer.show()
    } else {
        genresInputsContainer.hide()
    }

    return numGenres
}


/**
 * Add a new movie 
 * @param {newMovie} - the movie to be added to the db 
 */
function addMovie(newMovie){ 
    $.ajax({
        type: "POST",
        url: "add_movie",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(newMovie),
        success: function(response){
            let newMovieId = response.id 
            var newView =  $(`<button type="button" class="btn btn-warning">See it here</button>`)
            var newText = $("<div class='mr-2 mt-2'>New item successfully created!</div>")
            $("#new-entry-div").empty(); // Clear existing content
            $("#new-entry-div").append(newText, newView)
            $("#new-entry-div").addClass("small-margin")
            var redirectTo = "/view/" + newMovieId

            newView.on('click', function() {
                $(location).attr('href',redirectTo)
            })

        },
        error: function(request, status, error){
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}


function isValidImageUrl(url, onSuccess, onError) {
    var img = new Image()
    img.onload = function () {
        onSuccess()
    }
    img.onerror = function () {
        onError()
    }
    img.src = url
}



function validateForm() {

    var isValid = true

    $( ".warning" ).empty()

    // Validate summary
    if ($("#summary").val().trim()  === "") {
        $( "#summary-warning-div").append(`<div class="warning">Summary cannot be empty<div>`)
        $("#summary").val("").focus()
        isValid = false
    }

    // Validate stars
    if ($("#num-stars").val() === null || $("#num-stars").val() === "") {
        $( "#stars-warning-div").append(`<div class="warning">Select an option<div>`)
        isValid = false
    } else {
        for (let i = 0; i < $("#num-stars").val(); i++) {
            if ($(`#star-${i}`).val().trim() === "") {
                $(`#stars-warning-div`).append(`<div class="warning">Star ${i + 1} cannot be empty<div>`)
                $(`#star-${i}`).val("").focus()
                isValid = false
            }
        }
    }

    // Validate directors
    if ($("#num-directors").val() === null || $("#num-directors").val() === "") {
        $( "#directors-warning-div" ).append(`<div class="warning">Select an option<div>`)
        isValid = false
    } else {
        for (let i = 0; i < $("#num-directors").val(); i++) {
            if ($(`#director-${i}`).val().trim() === "") {
                $(`#directors-warning-div`).append(`<div class="warning">Director ${i + 1} cannot be empty<div>`)
                $(`#director-${i}`).val("").focus()
                isValid = false;
            }
        }
    }

    // Validate similar
    if ($("#num-similar").val() === null || $("#num-similar").val() === "") {
        $( "#similar-warning-div").append(`<div class="warning">Select an option<div>`)
        isValid = false
    } 

    // Validate genre
    if ($("#num-genres").val() === null || $("#num-genres").val() === "") {
        $( "#genre-warning-div").append(`<div class="warning">Select an option<div>`)
        isValid = false
    } else {
        for (let i = 0; i < $("#num-genres").val(); i++) {
            if ($(`#genre-${i}`).val().trim() === "") {
                $(`#genre-warning-div`).append(`<div class="warning">Genre ${i + 1} cannot be empty<div>`)
                $(`#genre-${i}`).val("").focus()
                isValid = false
            }
        }
    }



    // Validate budget
    if ($("#budget").val().trim()  === "") {
        $( "#budget-warning-div").append(`<div class="warning">Budget cannot be empty<div>`)
        $("#budget").val("").focus()
        isValid = false
    } else if(!/^\d+$/.test($("#budget").val().trim())) {
        $( "#budget-warning-div").append(`<div class="warning">Must be a number <span class="gray">do not include "$" or ","</span><div>`)
        $("#budget").focus()
        isValid = false
    }

    // Validate score
    if ($("#score").val().trim()  === "") {
        $( "#score-warning-div").append(`<div class="warning">Score cannot be empty<div>`)
        $("#score").val("").focus()
        isValid = false
    } else {
        let scoreFloat = parseFloat($("#score").val().trim())
    
        if (scoreFloat < 0 || scoreFloat > 10) {
            $("#score-warning-div").append('<div class="warning">Score must be between 0 and 10</div>')
            $("#score").val("").focus()
            isValid = false
        }
    }

    // Validate img
    var imageUrl = $("#image").val().trim()

    if (imageUrl === "") {
        $("#image-warning-div").append(`<div class="warning">Image cannot be empty</div>`)
        $("#image").val("").focus()
        isValid = false
    } // if the img is not valid them, the img tag will not be able to render it


    // Validate trailer
    if ($("#trailer").val().trim()  === "") {
        $( "#trailer-warning-div").append(`<div class="warning">Trailer cannot be empty<div>`)
        $("#trailer").val("").focus()
        isValid = false
    } else if(!$("#trailer").val().trim().includes("https://www.youtube.com/embed")) {
        $( "#trailer-warning-div").append(`<div class="warning">Must be a valid YouTube link: <span class="gray">i.e https://www.youtube.com/embed/eOrNdBpGMv8</span><div>`)
        $("#trailer").val("").focus()
        isValid = false
    }

    // Validate runtime
    if ($("#runtime-hours").val() === "") {
        $( "#runtime-warning-div").append(`<div class="warning">Runtime cannot be empty<div>`)
        $("#runtime-hours").val("").focus()
        isValid = false
    } else {
        if($("#runtime-minutes").val() === "") {
            $( "#runtime-warning-div").append(`<div class="warning">Runtime cannot be empty<div>`)
            $("#runtime-minutes").val("").focus()
            isValid = false
        } else {
            let minCurr = parseInt($("#runtime-minutes").val(), 10);
            if(minCurr < 0 || minCurr > 59) {
                $( "#runtime-warning-div").append(`<div class="warning">Runtime minute must be between 0-59<div>`)
                $("#runtime-minutes").focus()
                isValid = false
            }
        }
    }

    // Validate year
    if ($("#year").val().trim() === "") {
        $( "#year-warning-div").append(`<div class="warning">Year cannot be empty<div>`)
        $("#year").val("").focus()
        isValid = false
    } else {
        let yearCurr = parseInt($("#year").val().trim(), 10)
        if(yearCurr < 1939 || yearCurr > 2035) {
            $( "#year-warning-div").append(`<div class="warning">Year must be between 1939-2035<div>`)
            $("#year").val("").focus()
            isValid = false
        }
    }
    

    // Validate title
    if ($("#title").val().trim() === "") {
        $( "#title-warning-div").append(`<div class="warning">Title cannot be empty<div>`)
        $("#title").val("").focus()
        isValid = false
    }

    return isValid
}



$(document).ready(function() {

    var numDirectorsTotal
    var numStarsTotal
    var numSimilarTotal
    var numGenresTotal

    $( "#num-directors" ).on("change", function() {
        numDirectorsTotal = showDirectorsInput()
    })

    $( "#num-stars" ).on("change", function() {
        numStarsTotal = showStarsInput()
    })

    $( "#num-similar" ).on("change", function() {
        numSimilarTotal = showSimilarInput(similarMovies)
    })

    $( "#num-genres" ).on("change", function() {
        numGenresTotal = showGenresInput()
    })

    $( "#add-form" ).submit( function(event) {

        if(!validateForm()) {
            event.preventDefault()
            return
        }

        var titleValue = $( "#title" ).val()
        var yearValue = $( "#year" ).val()

        var runtimeHours = $( "#runtime-hours" ).val()
        var runtimeMinutes = $( "#runtime-minutes" ).val()
        var runtimeValue = runtimeHours + "h " + runtimeMinutes + "m"

        var trailerValue = $( "#trailer" ).val()
        var imageValue = $( "#image" ).val()
        var scoreValue = parseFloat($( "#score" ).val())

        var rawBudget = $( "#budget" ).val()
        var budgetValue = "$" + rawBudget.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
        var ratingValue = $( "#rating" ).val()
        var genresRaw = $( "#genre" ).val()

        var directorsValues = []
        for (let i = 0; i < numDirectorsTotal; i++) {
            var directorValue = $(`#director-${i}`).val()
            directorsValues.push(directorValue)
        }

        var starsValues = []
        for (let i = 0; i < numStarsTotal; i++) {
            var starValue = $(`#star-${i}`).val()
            starsValues.push(starValue)
        }

        var similarValues = []
        for (let i = 0; i < numSimilarTotal; i++) {
            var similarValue = $(`#similar-${i}`).val()
            similarValues.push(similarValue)
        }

        var genresValues = []
        for (let i = 0; i < numGenresTotal; i++) {
            var genreValue = $(`#genre-${i}`).val()
            genresValues.push(genreValue)
        }
        

        var summaryValue = $("#summary").val()

        // JSON format data to send 
        var newMovie = {
            "title": titleValue,
            "image": imageValue,
            "trailer": trailerValue,
            "year": yearValue,
            "summary": summaryValue,
            "runtime": runtimeValue,
            "director": directorsValues,
            "budget": budgetValue,
            "stars": starsValues,
            "score": scoreValue,
            "genres": genresValues,
            "similar": similarValues, 
            "rating":ratingValue
        } 

        // console.log(newMovie) 
        addMovie(newMovie)
        
        // clean the form 
        $("#add-form")[0].reset()
        for (let i = 0; i < numSimilarTotal; i++) {
            $(`#similar-${i}`).val('')
        }
        
        for (let i = 0; i < numGenresTotal; i++) {
            $(`#genre-${i}`).val('')
        }
        
        for (let i = 0; i < numStarsTotal; i++) {
            $(`#star-${i}`).val('')
        }
        
        for (let i = 0; i < numDirectorsTotal; i++) {
            $(`#director-${i}`).val('')
        }

        $( "#title" ).focus()
        window.scrollTo(0, 0)
        showDirectorsInput()
        showStarsInput()
        showSimilarInput(similarMovies)
        showGenresInput()

        event.preventDefault()
    })
    

})