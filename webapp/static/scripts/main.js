$(document).ready(function () { 

    $('#arquivo').change(function (e) {
        let fileName = e.target.files[0].name;
        let extensao = fileName.substring(fileName.length - 4, fileName.length)
        
        console.log("EXTENSAO:" + extensao)
        if (extensao != '.csv') {
            alert('Somente e aceito arquivos do tipo .csv !')
            $('#arquivo').val('');
        }
        
    });

    $('#limpar').click(function(){
        $('#arquivo').val('');
        url = window.location.origin + window.location.pathname;
        window.location.href = url;
    });


    loadClassActive();
  
})

function work() { /*...*/ }

if (document.readyState == 'loading') {
    // loading yet, wait for the event
    document.addEventListener('DOMContentLoaded', work);
} else {
    // DOM is ready!
    work();
}


function loadClassActive() {
    let page = window.location.pathname;

    if (page == '/gauss/') {
        $('#gauss').addClass('active')
    }
    else if (page == '/gaussjordan/') {
        $('#jordan').addClass('active')
    }
    else if (page == '/fatoracaolu/') {
        $('#fatoracao').addClass('active')
    }
}
