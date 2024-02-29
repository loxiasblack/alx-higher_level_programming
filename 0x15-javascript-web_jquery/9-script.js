$(document).ready(function () {
    $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data, status) {
        alert("Data: " + data + "\nStatus: " + status);
        for (index in data) {
            if (index == "hello"){
                hello = data[index];
                break;
            }
        }
        $("#hello").text(hello);
    });
});
