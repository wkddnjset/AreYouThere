// 새로운 기계 접속 시 유저 생성하기
createUser = function(){
    swal({
        title: "반갑습니다!",
        text: "닉네임을 적어주세요.",
        content: "input",
        button: "확인",
        closeOnClickOutside: false,
    })
    .then(name => {
        if (!name) throw null
     
        console.log(name)
        $.ajax({ 
            type: "POST", 
            url: DEFAULT_URL + "/user",
            data: {
                'device_id': uuid,
                'nickname': name,
            },
            dataType: "json", 
            success: function(response){
                console.log(response)
                if (response.status=='success'){
                    location.reload()
                }
                else{
                    swal({
                        title: response.message,
                        button: "확인",
                    });
                }
            },
            error: function(request, status, error){
            },
        });
    })
    .catch(err => {
        if (err) {
            swal("에러메세지", "The AJAX request failed!", "확인")
        } else {
            swal.stopLoading()
            swal.close()
        }
    });
}
// 페이지 로드 시 환영 메세지 or 유저 생성
$(document).ready(function(){
    $.ajax({ 
        type: "POST", 
        url: DEFAULT_URL + "/get/user",
        data: {
            'device_id': uuid,
        },
        dataType: "json", 
        success: function(response){
            console.log(response)
            if (response.status=='error'){
                createUser()
            }
            else{
                swal({
                    title: response.message,
                    button: "확인",
                })
            }
        },
        error: function(request, status, error){
        },
    });
})