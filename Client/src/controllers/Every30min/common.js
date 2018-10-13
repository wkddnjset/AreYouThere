
  

function createANDgetDaily(test){
	$.ajax({ 
        type: "POST", 
        url: DEFAULT_URL + "/daily",
        data: {
            'device_id': uuid,
            'test': test,
        },
        dataType: "json", 
        success: function(response){
            console.log(response)
            console.log(response.data)
            $(".work").removeClass('active')
            for (var i=0; i<response.data.length; i++){
            	$("#time_"+response.data[i]).addClass('active')
            }
            var work_hour = response.data.length * 0.5
            $('.work-hour span').text(work_hour.toString()+" Hrs")
        },
        error: function(request, status, error){
        },
    })
}

$(document).ready(function(){
	createANDgetDaily(1)
})

setInterval(function(){
	createANDgetDaily(2)
}, 1800000)
// 1800000
const {dialog} = require('electron').remote
setInterval(function(){
	// dialog.showMessageBox({
	// 	type : "info",
	// 	title: "Are You There",
	// 	message : "열심히 일하고 계신가요?!",
	// 	buttons : ["OK"],
	// })

	// alert("dd")
	// console.log($(window).focus())
}, 8000)
