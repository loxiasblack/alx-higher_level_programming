$(document).ready(function () {
    $('#btn_translate').click(function () {
      const code = $('#language_code').val();
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, function (data) {
        $('#hello').text(data.hello);
      });
    });
  });
