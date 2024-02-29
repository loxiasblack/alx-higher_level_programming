$(document).ready(function () {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status) {
        alert("Data: " + data + "\nStatus: " + status);
        const resuslts = data.results;
        let my_list = [];
        for (let index = 0; index < resuslts.length; index++) {
            for (element in resuslts[index]) {
                if (element == "title") {
                    my_list.push(resuslts[index][element])
                }
            }
        }
        $("#list_movies").text(my_list);            
    });
});
