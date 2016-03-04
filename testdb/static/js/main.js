function initEditStudentPage() {
	$('a.student-edit-form-link').click(function(event){
		var modal = $('#myModal');
		modal.modal('show');
		return false;
	});
}


$(document).ready(function(){
	initJournal();
	initGroupSelector();
	initDateFields();
	initEditStudentPage();
});
