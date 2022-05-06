$(document).ready(function () {
    console.log('Working From Base !');
    $('#modal-btn').click(function () {
        console.log('Profile Update Modal Opening...');
        $('.ui.modal').modal('show');
    })
    $('.ui.dropdown').dropdown();
});
