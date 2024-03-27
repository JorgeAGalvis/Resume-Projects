function displayHomeBanner(bannerData) {

    let container = $('<div>', { class: 'banner-container' })
    let img = $('<img>', { src: bannerData.image, alt: bannerData.alt, class: "img-banner" })
    let title = $('<h2>', { text: bannerData.title, class: 'banner-text' })

    let overlay = $('<div>', { class: 'overlay' });

    let description = $('<h5>', { text: bannerData.description, class: 'banner-text-d' })

    container.append(overlay);
    container.append(description)
    container.append(title)
    container.append(img)

    $( "#home-banner-div" ).append(container)
}

function displayTopRatedMovies(movies) {

    var topRatedTitle = $(`<div id="toprated-container-title" class="row">Top Rated Movies: </div>`)
    $(  "#toprated-movies-container" ).append(topRatedTitle)
    var topRatedDiv = $(`<div id="toprated-movies-div" class="col-12 d-flex justify-content-center"></div>`)

    $.each(movies, function(index, item) {
    
        let id = item.id
        let title = item.title
        let img = item.image

        var newMovie = $(`<div class="toprated-movie" data-id="${id}"></div>`)

        var imageSection = $(`<img class="toprated-img img-fluid" src="${img}" alt="${title}">`)
        $(newMovie).append(imageSection)

        var titleSection = $(`<div class="toprated-movie-title"></div>`)
        $(titleSection).html(title)
        $(newMovie).append(titleSection)

        $(topRatedDiv).append(newMovie)
        
    })

    $(  "#toprated-movies-container" ).append(topRatedDiv)

}


$(document).ready(function() {

    displayHomeBanner(bannerData)
    displayTopRatedMovies(topMovies)

    $(document).ready(function() {

        // Redirect to movie view 
        $( ".toprated-movie" ).click(function() {
            let movieId = $( this ).data("id")
            var redirectTo = "/view/" + movieId
            $(location).attr('href',redirectTo)
        })
    
    })

})
 