$(document).ready(function () {
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data, textStatus) {
        alert("here's the response: " + data);
        for (let names in data) {
            if (names == "name"){
                x = data[names]     
        }}
        $('#character').text(x)
    });
})
