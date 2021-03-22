$(document).ready( function () {
  var simples = $('#simples').DataTable({
    paging: false
  });

  var remedies = $('#remedies').DataTable({
    paging: false
  });

  $('#simples tbody').on( 'click', 'tr', function () {
    $(this).toggleClass('selected');
  });

  $('#remedies tbody').on( 'click', 'tr', function () {
    $(this).toggleClass('selected');
  });

  $('#dispense').click( function () {
    var simples_list = simples.rows('.selected').data()
    var remedies_list = remedies.rows('.selected').data()
    console.log(simples_list, remedies_list);
  });
});
