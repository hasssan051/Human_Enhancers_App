


let system_select = document.getElementById('system');
let organ_select = document.getElementById('organ');
let tissue_select = document.getElementById('tissue')

// for organ selectfield
system_select.onchange = function () {
    system = system_select.value;
    fetch('/organ/' + system).then(function (response) {
        response.json().then(function (data) {
            console.log(data)
            optionHTML='';
            //optionHTML = '<option value="None">None</option>';
            for (organ of data.organs) {
                optionHTML += '<option value="' + organ.organ + '">' + organ.organ + '</option>'
            }
            organ_select.innerHTML = optionHTML;
        });
    });
    }

// for tissue SelectField
organ_select.onchange = function () {
    organ = organ_select.value;
    fetch('/tissue/' + organ).then(function (response) {
        response.json().then(function (data) {
            console.log(data)
            optionHTML='';
            //optionHTML = '<option value="None">None</option>';
            for (tissue of data.tissues) {
                optionHTML += '<option value="' + tissue.tissue + '">' + tissue.tissue + '</option>'
            }
            tissue_select.innerHTML = optionHTML;
        });
    });
    }

// $(document).ready(function () {
//     $('#data').DataTable({
//         ajax: '/api/data',
//         columns: [
//         {data: 'name'},
//         {data: 'age', searchable: false},
//         {data: 'address', orderable: false, searchable: false},
//         {data: 'phone', orderable: false, searchable: false},
//         {data: 'email'}
//         ],
//     });
//     });

$(document).ready(function (){
    $('.columnSelector').on( 'click', function (e) {
        e.preventDefault();
        console.log($(this).attr('data-column'))
        var column = $('#data').DataTable().column($(this).attr('data-column'));
        column.visible( !column.visible() );
        $('#data').DataTable().columns.adjust().draw();
        $(this).toggleClass('btn-primary').toggleClass('btn-dark');
        // $(this).removeClass('btn-success').addClass('btn-primary ');
        // $(this).addClass('btn-success').removeClass('btn-primary ');
    });
   $(this).addClass('btn-primary');

});


$(document).ready(function () {
    var table = $('#data').DataTable({
        "columns": [
            {
                "data": 'HERD Accession', title:"HERD Accession", orderable: false
            },
            {
                "data": 'Chromosome', title:"Chromsome", orderable: false
            },
            {
                "data": "Chrom Start", title:"Chrom Start", orderable: true
            },
            {
                "data": "Chrom End", title:"Chrom End", orderable: false
            },
            {
                "data": "Prefix", title:"Prefix", orderable: false
            },
            {
                "data": "VISTA Overlap",title:"VISTA Overlap", orderable: false
            },
            {
                "data": "Contains VISTA",title:"Contains VISTA", orderable: false
            },
            {
                "data": "eRNA Overlap",title:"eRNA Overlap", orderable: false
            },
            {
                "data": "Contains eRNA",title:"Contains eRNA", orderable: false
            }
        ],
        "order": [[ 2, 'asc' ]],
        
        "scrollY": "500px",
        "scrollX": "true",
        "scrollCollapse": "false",
        "responsive": "true",
        "searching":false,
        "lengthChange": false
    } );
    // new $.fn.dataTable.FixedHeader( table );
  });
