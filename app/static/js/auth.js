$(document).ready(function() {

    $('#login-button').click(function() {

        let login = $('#login-input').val()
        let password = $('#pass-input').val()

        request = $.ajax({
            type: "POST",
            url: "auth",
            data: {login: login, password: password},
            dataType: "json",
        });

        request.done(function(response) {
            if (response.success == true) {
                $('#eyes-error').attr('class', 'invisible');
                $('#eyes-success').attr('class', 'visible');
                setTimeout(() => {
                    window.location.replace('/cp')
                }, 3000);
            } else {
                $('#eyes-error').attr('class', 'visible');
                setTimeout(() => {
                    $('#eyes-error').attr('class', 'invisible')
                }, 3000);
                
            }

        });

    });

});
