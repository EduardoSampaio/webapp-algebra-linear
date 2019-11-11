$(document).ready(function () { 

    $('#arquivo').change(function (e) {
        var fileName = e.target.files[0].name;
        console.log(e.target.files[0]);
        
    });

    $('#limpar').click(function(){
        $('#arquivo').val('');
      //  let url =  window.location.hostname
        window.location.href = url
    });

    $(window).on('load', function () {
   
    })


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
