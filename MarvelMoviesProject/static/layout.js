// This doc is available to all pages 
$(document).ready(function() {

    // Search bar error checking prevention
    $('#search-form').submit(function(event) {
        var query = $.trim($(" #search-input").val())
        if (!query) {
            event.preventDefault()
            $( "#search-input" ).val("").focus()
        }
    })
    
})
 