$(function() {
    $("#newvid").submit(function(event) {
        event.preventDefault();
        var form = $(this);
        // Send the data using post
        $.ajax({
          type: "POST",
          url: form.attr('action'),
          data: form.serialize(),
          beforeSend: function() {
            $('#statusMessage').attr('class', 'd-none');
            setTimeout(function() { $('#spinner').attr('class', 'spinner-border text-danger mt-3'); }, 10);
            console.log("before send called");
          },
          success: function(data) {
            var message;
            var color;
            if (data.video_exists) {
                message = 'Video already exists.';
                color = 'text-danger';
            } else if (data.is_valid) {
                message = 'Video added to library.';
                color = 'text-success';
            } else {
                message = 'YouTube video does not exist or URL is invalid.';
                color = 'text-danger';
            }
            $('#spinner').attr('class', 'd-none');
            $('#statusMessage').attr('class', 'mt-3 mb-0 ' + color);
            $('#statusMessage').html(message);
          }
        });
    });
});