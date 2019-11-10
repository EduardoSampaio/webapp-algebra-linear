$(document).ready(function () { 

    $('#arquivo').change(function (e) {
        var fileName = e.target.files[0].name;
        console.log(fileName);
        
    });

    $('#limpar').click(function(){
        $('#arquivo').val('');
      //  let url =  window.location.hostname
        window.location.href = url
    });


    loadClassActive();
  
})


function loadClassActive() {
    let page = window.location.pathname;

    if (page == '/gauss/') {
        console.log(page)
        $('#gauss').addClass('active')
    }
    else if (page == '/gaussjordan/') {
        $('#jordan').addClass('active')
    }
    else if (page == '/fatoracaolu/') {
        $('#fatoracao').addClass('active')
    }
}
