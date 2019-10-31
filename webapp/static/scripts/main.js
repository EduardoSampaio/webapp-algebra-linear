$(document).ready(function () { 

    $('#arquivo').change(function (e) {
        var fileName = e.target.files[0].name;
        console.log(fileName);
        
    });
  
})

