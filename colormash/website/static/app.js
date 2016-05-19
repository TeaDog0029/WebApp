// Javascript

var main = function{
    $('#in-line').click(function(event){
        var url_winner = event.target.src;
        console.log(url_winner);
    });
}

$(document).ready(main);