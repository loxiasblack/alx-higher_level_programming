$(document).ready( function () {
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(response => {
        if (!response.ok) {
            throw new Error("response was not ok");
        }
        return response.json()
    })
    .then(data => {
        const hello = data["hello"];
        $('#hello').text(hello);
    })
    .catch(error =>{
        console.error("fetch error:", error);
    });
});
