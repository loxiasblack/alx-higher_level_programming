$(document).ready(function () {
    fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
    .then(response => {
        if (!response.ok) {
            throw new Error("response was not ok");
        }
        return response.json();
    })
    .then(data => {
        const results = data.results;
        results.forEach(element => {
            const name = `<li>${element['title']}</li>`
            $('#list_movies').append(name);
        });
    })
    .catch(error =>{
        console.error('Fetch error:', erorr)
    });
});
