


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
