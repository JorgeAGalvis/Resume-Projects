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
        })

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
            placeholder: "Similar Movie " + (i + 1)
        })

        $.each(similarMovies, function (index, value) {
            var option = $(`<option similar-${i} data-id=${value.id} value="${index+1}">${value}</option>`)
            select.append(option)
        })

        inputGroup.append(select)
        similarInputsContainer.append(inputGroup)
    }

    if (numSimilar > 0) {
        similarInputsContainer.show()
    } else {
        similarInputsContainer.hide()
    }

    return numSimilar
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


function populateFormFields(movieToEdit, similarMoviesToEdit) {

    $('#title').val(movieToEdit.title)
    $('#year').val(movieToEdit.year)

    let [hours, minutes] = movieToEdit.runtime.split(' ') 
    $('#runtime-hours').val(parseInt(hours, 10) || 0)
    $('#runtime-minutes').val(parseInt(minutes, 10) || 0)

    $('#trailer').val(movieToEdit.trailer)
    $('#image').val(movieToEdit.image)
    $('#score').val(movieToEdit.score)
    $('#rating').val(movieToEdit.rating)


    let plainBudget = movieToEdit.budget.replace(/[$,]/g, '');
    let budgetValue = parseInt(plainBudget, 10);
    $('#budget').val(budgetValue)


    $('#num-genres').val(movieToEdit.genres.length)
    $.each(movieToEdit.genres, function(index, genre) {
        var genreInput = $("<input>").attr({
            type: "text",
            class: "form-control",
            id: `genre-${index}`,
            placeholder: "Genre " + (index + 1),
            value: genre
        })
        $('#genres-inputs').append(genreInput)
    })


    $('#num-similar').val(movieToEdit.similar.length)
    $.each(similarMoviesToEdit, function(index, similar) {
        var similarSelect = $("<select>").attr({
            class: "form-control",
            id: `similar-${index}`,
            "data-id": similar.id,
            disabled: true  
        })
        
        var option = $("<option>").attr({
            value: similar.title,
            id: `similar-${index}`,
            "data-id": similar.id,
            selected: true 
        }).text(similar.title)

        similarSelect.append(option)

        $('#similar-inputs').append(similarSelect)
        
    })
    
    $('#num-directors').val(movieToEdit.director.length)
    $.each(movieToEdit.director, function(index, director) {
        var directorInput = $("<input>").attr({
            type: "text",
            class: "form-control",
            id: `director-${index}`,
            placeholder: "Director " + (index + 1),
            value: director
        })
        $('#directors-inputs').append(directorInput)
    })
    

    $('#num-stars').val(movieToEdit.stars.length)
    $.each(movieToEdit.stars, function(index, star) {
        var starInput = $("<input>").attr({
            type: "text",
            class: "form-control",
            id: `star-${index}`,
            placeholder: "Star " + (index + 1),
            value: star
        })
        $('#stars-inputs').append(starInput)
    })


    $('#summary').val(movieToEdit.summary)
}


/**
 * Add a new movie 
 * @param {newMovie} - the movie to be added to the db 
 */
function editMovie(editedMovie){ 
    $.ajax({
        type: "POST",
        url: "/edit_movie",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(editedMovie),
        success: function(response){
            let editedMovieId = response.id 
            var redirectTo = "/view/" + editedMovieId
            $(location).attr('href',redirectTo)
        },
        error: function(request, status, error){
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
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
                isValid = false
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
    } 


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
            let minCurr = parseInt($("#runtime-minutes").val(), 10)
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

    populateFormFields(movieToEdit, similarMoviesToEdit)
    var numDirectorsTotal = $( "#num-directors" ).val()
    var numStarsTotal = $('#num-stars').val()
    var numSimilarTotal = $('#num-similar').val()
    var numGenresTotal =  $('#num-genres').val()
    
    
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

    $( "#num-similar" ).click(function() {
        numSimilarTotal = showSimilarInput(similarMovies)
    })
    
    
    $( "#edit-form" ).submit(function(event) {

        if(!validateForm()) {
            event.preventDefault()
            return
        }

        // all of this is the same fixing the error checking of add 
        // should just be copy and paste here
        var titleValue = $( "#title" ).val()
        var yearValue = $( "#year" ).val()

        var runtimeHours = $( "#runtime-hours" ).val()
        var runtimeMinutes = $( "#runtime-minutes" ).val()
        var runtimeValue = runtimeHours + "h " + runtimeMinutes + "m"

        var trailerValue = $( "#trailer" ).val()
        var imageValue = $( "#image" ).val()
        var scoreValue = parseFloat($( "#score" ).val())  // make sure this is sent as a float

        var rawBudget = $( "#budget" ).val()
        var budgetValue = "$" + rawBudget.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
        var ratingValue = $( "#rating" ).val()
        var genresRaw = $( "#genre" ).val()

        var directorsValues = $( "#num-directors" ).val()
        
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
            var similarValue = $(`#similar-${i} option:selected`).data("id").toString()
            if(similarValue === 'undefined' || similarValue === null) {
                similarValue = $(`#similar-${i}`).val();
            }
            similarValues.push(similarValue)
        }
        

        var genresValues = []
        for (let i = 0; i < numGenresTotal; i++) {
            var genreValue = $(`#genre-${i}`).val()
            genresValues.push(genreValue)
        }

        
        var summaryValue = $("#summary").val()


        // JSON format data to send 
        var editedMovie = {
            "id": movieToEdit.id,
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

        //console.log(editedMovie)
        editMovie(editedMovie)

        //event.preventDefault()
    })

    // if discard, redirect to the view without saving the changes 
    $( "#discard" ).click(function(event) {
        event.preventDefault()
        $( "#confirm-div" ).empty()
        $( "#confirm-div" ).addClass("confirm-div-style")

        let confimDiscard=  $(`<button type="button" class="btn btn-warning button-dc-margin">Discard</button>`)
        let confimCancel =  $(`<button type="button" class="btn btn-light button-dc-margin">Cancel</button>`)
        let buttonsDiv = $(`<div class="button-container" id="button-container-style"></div>`)

        $(buttonsDiv).append(confimDiscard, confimCancel)

        let confirmText =  $(`<div>Are you sure you want to discard changes?</div>`)

        $( "#confirm-div" ).append(confirmText, buttonsDiv)

        window.scrollTo(0, 0);

        $(confimDiscard).click(function() {
            let movieId = movieToEdit.id
            var redirectTo = "/view/" + movieId 
            $(location).attr('href',redirectTo)
        })

        $(confimCancel).click(function() {
            $( "#confirm-div" ).removeClass("confirm-div-style")
            $( "#confirm-div" ).empty()
        })

    })

})
