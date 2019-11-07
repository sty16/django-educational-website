$(function(){
    $('#CodeUploadBtn').click(function(){
        var formdata = new FormData($('#code_form')[0])
        var user_id = $('#id_userinfo');
        user_id.removeAttr("disabled");
        user_name = user_id.attr("value");
        console.log(user_name);
        formdata.append("userinfo", user_name);
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
        var dis_info = false;
        if (send){
            $.ajax({
                cache:false,
                type:"post",
                url:"/coding/upload/",
                async:false,
                data:formdata,
                traditional:true, //为必须内容 　　
                processData: false, //为必须内容
                contentType: false, //为必须内容
                beforeSend:function(XMLHttpRequest){
                    $('#CodeUploadBtn').val("发送中...");
                    $('#CodeUploadBtn').attr('disabled',true);
                },
                success:function(data) {
                    if (data.status == 'success'){
                        alert("文件上传成功");
                        location.href = "/users/myuncheckedcode/"
                    }else if(data.status == 'wrong'){
                        if(confirm("上传文件存在语法错误"))
                        {
                            location.href = "/coding/upload/";
                        }else{
                            location.href = "/coding/upload/";
                        }
                    }
                },
                complete: function(XMLHttpRequest){
                    $('#CodeUploadBtn').val("上传文件");
                    $('#CodeUploadBtn').removeAttr("disabled");
                }
            });
        }
    });
    
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
    $('.Favnum').on('click', function(){
        // this.className = "collected fr Favnum";
        // this.textContent = (parseInt(this.textContent) + 1).toString();
        var file_id = $(this).attr("name");
        file_id = String(file_id);
        console.log(file_id);
        var csrfToken = $("[name='csrfmiddlewaretoken']").val();
        var display = false;
        $.ajax({
            cache:false,
            type:"post",
            url:"/coding/fav_num/",
            async:false,
            data:{ "file_id": file_id, "csrfmiddlewaretoken": csrfToken},
            success:function(data){
                if (data.status=="success")
                {
                    display = true;
                }else{
                    alert('您已点赞该代码');
                }
            }
        });
        if (display){
            // this.className = "collected fr Favnum";
            // location.reload()
            this.className = "collected fr Favnum";
            this.textContent = (parseInt(this.textContent) + 1).toString();
        }
    })
});

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
