var colors = ['#1AAEDF', 'F0992A', '#D91B5B', '#F7D947', '#8DC74D', '#F0DEA4', '#F9C8A7', '#85235B'];

function main(){
	var i = 0;
	$('.category-content').each(function(){
		$(this).css('background-color', colors[i])
		i++;
	});
	
	if($('.title').text() === 'Categorías'){
		$('body').css('background-color', '#EEEEEE');
	}

	$('.subcategory:first-child').addClass('active');
	
	$('#categories tbody tr').on('click', function(){
		$('#btn-reported').removeClass('btn-custom');
		$('#row-selected').removeAttr('id');
		$(this).attr('id', 'row-selected');
	});

	$('#agregar_url').on('submit', function(e){
		e.preventDefault();
		$.ajax({
			url : '/url/add',
			type: 'POST',
			data: {
				link: $('#row-selected #url').text()
			},
			success : function(data){
				$('#btn-reported').addClass('btn-custom');
				alert(JSON.stringify(data.msj));
			},
			error : function(error){
				console.log(error);
			}
		});
	});

	
	$('#categories').DataTable({
		autoFill: true,
		responsive: true,
	});	
}


$(document).on('ready', main);