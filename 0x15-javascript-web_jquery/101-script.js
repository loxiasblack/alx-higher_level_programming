$(document).ready(function () {
    $('#add_item').on('click', function () {
        const item = $('<li>Item</li>');
        $('.my_list').append(item)
    });
    $('#remove_item').on('click', function () {
        $('.my_list li:last').remove();
    });
    $('#clear_list').on('click', function () {
        $('.my_list').empty();
    });
});
