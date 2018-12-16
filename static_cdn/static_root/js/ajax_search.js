$(document).ready(function () {
    // Ajax Search
    let searchForm = $(".search-form");
    let searchInput = searchForm.find("[name='q']");
    let typingTimer;
    let typingInterval = 1500;  // .5s

    let searchBtn = searchForm.find("[name='submit']");

    searchInput.keyup(function (event) {
        // key realised
        clearTimeout(typingTimer);
        typingTimer = setTimeout(performSearch, typingInterval)
    });

    searchInput.keydown(function (event) {
        // key pressed
        clearTimeout(typingTimer);
    });

    function searching() {
        searchBtn.addClass("disabled");
        searchBtn.html("<i class='fa fa-spin fa-spinner'></i>");
    }

    function performSearch() {
        searching();
        let query = searchInput.val();
        setTimeout(function () {
            window.location.href='/search/?q=' + query
        }, 500)
    }
});
