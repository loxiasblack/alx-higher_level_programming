function translate () {
    const code = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${code}`, function (data) {
      $('#hello').text(data.hello);
    });
  }
  
  $(document).ready(function () {
    $('#language_code').on('keypress', function (e) {
      if (e.key === 'Enter') {
        translate();
      }
    });
    $('#btn_translate').click(function () {
      translate();
    });
  });
