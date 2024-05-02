$(document).ready( function () {
    fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
    .then(response => {
        if (!response.ok) {
            throw new Error('response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const characterName = data.name;
        if (characterName) {
            $('#character').text(characterName);
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
});
