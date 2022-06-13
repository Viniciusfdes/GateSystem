$(document).ready(function () {
    $('#bootstrapdatatable').DataTable({
      "language": {
        "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese-Brasil.json"
      },
      "aLengthMenu": [[2, 4, 10, 20, -1], [2, 4, 10, 20, "All"]],
      "iDisplayLength": 3
    });
  });