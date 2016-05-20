// Javascript


var main = function(){
    $("button").click(function(){
    	alert("You clicked!");
    	var winner_pk = $(this).attr("name");
    	var loser_pk = $(this).next().attr("name");
    	alert("pk = " + winner_pk);
        $("input[name='winner_pk']").val(winner_pk);
        $("input[name='loser_pk']").val(loser_pk);
        alert("alert");
	});
}

$(document).ready(main);

