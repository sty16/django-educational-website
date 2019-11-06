$(function(){
    $('#jsSendCode').on('click', function(){
        var send = true;
        formdata = $('form').serialize()
        var $check = $('form#mobile_register_form input');
        for (let i=0; i<3;i++)
        {  
            let value = $check[i].value
            if (value == null || value == "" ){
                $check[i].focus();
                send = false;
                break;
            }
        }
        if (send){
            $.ajax({
                cache:false,
                type:"get",
                url:"/users/mobileregister/",
                async:true,
                data:formdata,
                beforeSend:function(XMLHttpRequest){
                    $(this).val("发送中...");
                    $(this).attr('disabled',true);
                },
                success:function(data){
                    if (data.status=="success"){
                        $('#jsMobileTips')[0].textContent = data.msg
                        $('#jsMobileTips').show()
                    }else{
                        $('#jsMobileTips')[0].textContent = data.msg
                        $('#jsMobileTips').show()
                    }
                },
                complete: function(XMLHttpRequest){
                    $(this).val("发送验证码");
                    $(this).removeAttr("disabled");
                }
            });
        }
    })
    $('#id_username').on('click', function(){
        $('#jsMobileTips').hide()
    });
    $('#id_mobile').on('click', function(){
        $('#jsMobileTips').hide()
    });
    $('#id_password').on('click', function(){
        $('#jsMobileTips').hide()
    });
    $('#jsPhoneRegCaptcha').on('click', function(){
        $('#jsMobileTips').hide()
    });
    $('#jsMobileRegBtn').on('click',function(){
        var $verify = $('#jsPhoneRegCaptcha');
        formdata = $('form').serialize();
        var send = true;
        value = $verify.attr("value");
        if (value == ""||value == null)
        {   
            $('#jsMobileTips')[0].textContent = "请填写验证码"
            $('#jsMobileTips').show();
            send = false;
        }
        if (send){
            $.ajax({
                cache:false,
                type:"post",
                url:"/users/mobileregister/",
                async:true,
                data:formdata,
                beforeSend:function(XMLHttpRequest){
                    $(this).attr('disabled',true);
                },
                success:function(data){
                    if (data.status=="success"){
                        $('#jsMobileTips')[0].textContent = data.msg
                        $('#jsMobileTips').show()
                    }else{
                        $('#jsMobileTips')[0].textContent = data.msg
                        $('#jsMobileTips').show()
                    }
                },
                complete: function(XMLHttpRequest){
                    $(this).removeAttr("disabled");
                }
            });
        }
    })
});