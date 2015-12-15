var colors = ['#1AAEDF', 'F0992A', '#D91B5B', '#F7D947', '#8DC74D', '#F0DEA4', '#F9C8A7', '#85235B'];

	var i = 0;
	$('.category-content').each(function(){
		$(this).css('background-color', colors[i])
		i++;
	});
	
	if($('.title').text() === 'Categorías'){
		$('body').css('background-color', '#EEEEEE');
	}

	$('.subcategory:first-child').addClass('active');

	$('#categories').DataTable({
  		"columns": [
    		{ "width": "20px" },
    		{ "width": "20px" },
    		{ "width": "20px" },
    		{ "width": "20px" },
    		{ "width": "20px" },
    		{ "width": "20px" },
    		{ "width": "20px" },
    		{ "width": "20px" }
  		]

	});	
	
	$('#categories tbody tr').on('click', function(){
		$('#btn-reported').removeClass('btn-custom');
		document.getElementById('btn-reported').disabled = false;
		$('#row-selected').removeAttr('id');
		$(this).attr('id', 'row-selected');
	});

	document.getElementById('btn-reported').disabled = true;

	$('#agregar_url').on('submit', function(e){
		e.preventDefault();
		$.ajax({
			url : '/url/add',
			type: 'POST',
			data: {
				link: $('#row-selected #url').text()
			},
			success : function(data){
				swal({
				  title: "¿Estás seguro?",
				  text: "Sólo reporta las direcciones que no funcionen correctamente",
				  type: "warning",
				  showCancelButton: true,
				  confirmButtonColor: "#DD6B55",
				  confirmButtonText: "Reportar",
				  closeOnConfirm: false
				},
				function(){
				  swal("Reportada!", "Revisaremos la dirección en breve.", "success");
				});
			},
			error : function(error){
				console.log(error);
			}
		});
	});