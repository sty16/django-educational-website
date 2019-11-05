$(function(){
    $('#CodeUploadBtn').click(function(){
        var formdata = new FormData($('#code_form')[0])
        var user_id = $('#id_userinfo');
        user_id.removeAttr("disabled");
        user_name = user_id.attr("value");
        console.log(user_name);
        formdata.append("userinfo", user_name);
        // if ( !formdata.codefile){
        //     alert('您还没有选择文件')
        //     return 1
        // }
        // $('form.exform input').each(function(){
        //     var value = $(this).attr("value");
        //     value = value.trim();
        //     if (value ==null || value == "" ){
        //         $(this).focus();
        //     }
        // });
        var send = true;
        var $check = $('form.exform input');
        for (let i = 0;i<$check.length;i++)
        { 
            let value = $check[i].value
            if (value ==null || value == "" ){
                $check[i].focus();
                send = false;
                break;
            }
        }
        if (send){
            $.ajax({
                cache:false,
                type:"post",
                url:"/coding/upload/",
                async:true,
                data:formdata,
                traditional:true, //为必须内容 　　
                processData: false, //为必须内容
                contentType: false, //为必须内容
                beforeSend:function(XMLHttpRequest){
                    $('#CodeUploadBtn').val("发送中...");
                    $('#CodeUploadBtn').attr('disabled',true);
                },
                complete: function(XMLHttpRequest){
                    $('#CodeUploadBtn').val("上传文件");
                    $('#CodeUploadBtn').removeAttr("disabled");
                },
                success: function(result) {
                    if (result.status =='failure'){
                        alert("文件存在语法错误")
                    }else{
                        $('html').html(result)
                    }
                  
                }
            });
        }
        // else{
        //     alert("该项为必填项目")
        // }
    })
    
    $('.getcode').on('click', function(){
        var obj = $(this);
        var id = obj.attr("id");
        var formdata = new FormData();
        var csrfToken = $("[name='csrfmiddlewaretoken']").val();
        formdata.append("File_id", id);
        $.ajax({
            cache:false,
            type:"post",
            url:"/coding/download/",
            async:true,
            data:{'File_id':id, "csrfmiddlewaretoken": csrfToken},
            beforeSend:function(XMLHttpRequest){
                obj.val("下载中...");
                obj.attr('disabled',true);
            },
            success:function(data){
                if (data){
                    var $count_obj = $('i#' + id);
                    console.log($count_obj)
                    $count_obj[0].textContent = (parseInt($count_obj[0].textContent) + 1).toString();
                    const filedata = data
                    const blob = new Blob([filedata])
                    const bloburl = window.URL.createObjectURL(blob)
                    const a = document.createElement('a')
                    a.download = 'template.py'
                    a.href = bloburl
                    a.style.display = 'none'
                    document.body.appendChild(a)
                    a.click()
                    document.body.removeChild(a)
                }else{
                    alert("对不起，网络错误，请稍后重试或联系管理员")
                }
                // if (data.status =="success"){
                //     location.href = '/media/' + data.FilePath;
                //     var count_obj = $('i#' + id);
                //     console.log(count_obj)
                //     count_obj[0].textContent = (parseInt(count_obj[0].textContent) + 1).toString();
                // }else{
                //     // window.location.href = '/media/' + data.FilePath;
                //     alert("对不起，网络错误，请稍后重试或联系管理员")
                // }
            },
            complete: function(XMLHttpRequest){
                obj.val("下载代码");
                obj.removeAttr("disabled");
            }
    });
    })
});
// function download_file(btn){
//     var obj = $(btn);
//     var id = obj.attr("id");
//     var formdata = new FormData();
//     formdata.append("File_id", id);
//     alert(id)
//     $.ajax({
//         cache:false,
//         type:"post",
//         url:"coding/download/",
//         async:true,
//         data:formdata,
//         beforeSend:function(XMLHttpRequest){
//             obj.val("下载中...");
//             obj.attr('disabled',true);
//         },
//         complete: function(XMLHttpRequest){
//             obj.val("下载文件");
//             obj.removeAttr("disabled");
//         },
//         success:function(data){
//             if (data.status == True){
//                 window.location.href = data.FilePath;
//             }else{
//                 alert("对不起，网络错误，请稍后重试或联系管理员")
//             }
//         }
//     });
//     }
function QueryFilename(file_id){
    var filename = "";
    send_data = {"file_id":file_id};
    $.ajax({
        cache:false,
        type:"get",
        url:"/coding/download/",
        async:false,  //待修改
        data:send_data,
        dataType:'json',
        success:function(data){
            if (data.status=="success"){
                filename = data.filename;
            }
        }
    });
    return filename;
}
