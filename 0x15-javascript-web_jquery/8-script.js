$(document).ready(() => {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (datas) => {
        $.each(datas.results, function(index, film) {
            $('UL#list_movies').append('<li>' + film.title + '</li>');
        });
    });
});
