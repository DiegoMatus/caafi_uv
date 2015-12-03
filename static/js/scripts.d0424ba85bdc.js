function main(){
	$('#categories').DataTable({
		autoFill: true,
		responsive: true,
	});
}


$(document).on('ready', main);