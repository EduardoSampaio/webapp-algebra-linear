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
  
})

