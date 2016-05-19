// Javascript


var main = function(){
    $('.welcome_page_form').click(function(event){
    	//alert('app.js is running');
    	var winner_pk = event.attr("name");
    	var loser_pk = event.next().attr("name");
    	alert('winner_pk = 'winner_pk);
    	var first_row_table = $('#vote_pk').first();
		console.log(winner_pk);
		console.log(loser_pk);

		first_row_table.val(winner_pk);
		first_row_table.next().val(loser_pk);
    });
}

$(document).ready(main);

