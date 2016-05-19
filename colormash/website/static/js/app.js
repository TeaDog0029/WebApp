// Javascript


var main = function(){
    $("button").click(function(){
    	var winner_pk = $(this).attr("name");
    	var loser_pk = $(this).next().attr("alt");
    	//alert("pk = " + winner_pk);
        var aux_a = $("input[name='winner_pk']").val(winner_pk);
        $("input[name='loser_pk']").val(loser_pk);
        alert("input winner = " + aux_a);



  //   	var first_row_table = $().attr('vote_pk').first();
		// console.log(winner_pk);
		// console.log(loser_pk);

		// first_row_table.val(winner_pk);
		// first_row_table.next().val(loser_pk);
    });
}

$(document).ready(main);

