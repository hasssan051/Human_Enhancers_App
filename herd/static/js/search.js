
let system_select = document.getElementById('System');
let organ_select = document.getElementById('Organ');
let tissue_select = document.getElementById('Tissue');
let prevHist_select = $("#queryHistDropDown").length ? document.getElementById('queryHistDropDown') :null;

// for organ selectfield
system_select.onchange = function () {
    system = system_select.value;
    fetch('/organ/' + system).then(function (response) {
        response.json().then(function (data) {
            optionHTML = '';
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
            optionHTML = '';
            //optionHTML = '<option value="None">None</option>';
            for (tissue of data.tissues) {
                optionHTML += '<option value="' + tissue.tissue + '">' + tissue.tissue + '</option>'
            }
            tissue_select.innerHTML = optionHTML;
        });
    });
}

// fill in previous historical into dropdown
$(document).ready(function (){
    if(prevHist_select)
    {
        fetch("/api/prevQueries").then(function (response){
            response.json().then(function (data) {
                optionHTML = '';
                for(search of data.searches){
                    if (search.search == "None"){
                        optionHTML += '<option value="' + 'None' + '">' + 'None'  + '</option>';
                    }else{
                        optionHTML += '<option value="' + JSON.stringify(search.search).replaceAll("\"","'") + '">' + JSON.stringify(search.search)  + '</option>';
                    }
                }
                prevHist_select.innerHTML = optionHTML;
            });
        });
    }
});

// fills query form based on dropdown selection
$(function(){
    if(prevHist_select)
    {
        prevHist_select.onchange = (function(){
            if(this.value === 'None'){
                $('#Chromosome').val('None');
                $('#chromStart').val("");
                $('#chromEnd').val("");
                $('#System').val('All');
                $('#Organ').val('All');
                $('#Tissue').val('All');
                $('#checkBoxDisease').prop("checked", false);
                $('#checkBoxTreated').prop("checked", false);
            }
            else{
                var form_values = JSON.parse(this.value.replaceAll("\'","\""));
                $('#Chromosome').val(form_values['Chromosome']);
                $('#chromStart').val(form_values['chromStart']);
                $('#chromEnd').val(form_values['chromEnd']);
                $('#System').val(form_values['System']);
                $('#Organ').val(form_values['Organ']);
                $('#Tissue').val(form_values['Tissue']);
                $('#checkBoxDisease').prop("checked", form_values['Disease']);
                $('#checkBoxTreated').prop("checked", form_values['Treated']);
            }
            
        });
    }

});


// toggles column visibility
$(document).ready(function () {
    $('.columnSelector').on('click', function (e) {
        e.preventDefault();
        
        var column = $('#data').DataTable().column($(this).attr('data-column'));
        column.visible(!column.visible());
        $('#data').DataTable().columns.adjust().draw();
        $(this).toggleClass('btn-primary').toggleClass('btn-dark');
        // $(this).removeClass('btn-success').addClass('btn-primary ');
        // $(this).addClass('btn-success').removeClass('btn-primary ');
    });
    $(this).addClass('btn-primary');

});



$(document).ready(function () {

    var table = $('#data').DataTable({
        "responsive": "true",
        "dom": "<'row' t>" + "<'row '<'col-md-12 col-lg-2'B><'col-md-12 col-lg-5'i><'col-md-12 col-lg-5'p>>",

        "columns": [
            {
                "data": 'HERD Accession', title: "HERD Accession", orderable: false
            },
            {
                "data": 'Chromosome', title: "Chromsome", orderable: false
            },
            {
                "data": "Chrom Start", title: "Chrom Start", orderable: true
            },
            {
                "data": "Chrom End", title: "Chrom End", orderable: false
            },
            {
                "data": "Prefix", title: "Prefix", orderable: false,searchable:true
            },
            {
                "data": "VISTA Overlap", title: "VISTA Overlap", orderable: false,
                "render": function(data, type, row, meta){
                    if(type === 'display'){
                        data = '<a href="https://enhancer.lbl.gov/cgi-bin/imagedb3.pl?form=presentation&show=1&experiment_id='+ data + '&organism_id=1 ">' + data + '</a>';
                    }
                   
                    return data;
                 }
            },
            {
                "data": "Contains VISTA", title: "Contains VISTA", orderable: false,
                "render": function(data, type, row, meta){
                    if(type === 'display'){
                        data = '<a href="https://www.enhancer.lbl.gov/cgi-bin/imagedb3.pl?form=presentation&show=1&experiment_id='+ data + '&organism_id=1 ">' + data + '</a>';
                    }
        
                    return data;
                 }
            },
            {
                "data": "eRNA Overlap", title: "eRNA Overlap", orderable: false
            },
            {
                "data": "Contains eRNA", title: "Contains eRNA", orderable: false
            }
        ],
        "order": [[2, 'asc']],

        "scrollY": "500px",
        "scrollX": "true",
        "scrollCollapse": "false",

        // "searching": true,
        "lengthChange": false
    });
    $('#data').DataTable().columns.adjust();
    $("#data_wrapper").prepend($('#columnVisibilityBtns'));

    var prefixIndex = 4;
    
    $('#annotationFilter li').on('click', function () {
        var anot= ($(this).attr('data-value'));
        console.log(anot)
        if(anot ==="")
        {
            table.search('').columns().search('').draw();
        }
        else{
            table.columns(4).search(anot).draw();
        }
               
    });
   
    table.draw();

    // new $.fn.dataTable.FixedHeader( table );
});


