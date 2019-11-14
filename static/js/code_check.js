$(function(){
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
                    const filedata = data
                    const blob = new Blob([filedata])
                    let file_name = QueryFilename(id)
                    const bloburl = window.URL.createObjectURL(blob)
                    const a = document.createElement('a')
                    a.download = file_name;
                    a.href = bloburl
                    a.style.display = 'none'
                    document.body.appendChild(a)
                    a.click()
                    document.body.removeChild(a)
                }else{
                    alert("对不起，网络错误，请稍后重试或联系管理员")
                }
            },
            complete: function(XMLHttpRequest){
                obj.val("下载代码");
                obj.removeAttr("disabled");
            }
    });
    })
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
    $('.codecheck').on('click',function(){
        var code_obj = $(this);
        var code_id = String(code_obj.attr('name'));
        console.log(code_id);
        var check_result = $("input[name=" + code_id + "]:checked").val();
        var csrfToken = $("[name='csrfmiddlewaretoken']").val();
        console.log(check_result);
        if (check_result != undefined){
            send = confirm('确认提交结果');
        }else{
            alert('您还没有选择审核结果');
        }
        if(send){
            $.ajax({
            cache:false,
            type:"post",
            url:"/coding/code_check/",
            async:true,
            data:{'File_id':code_id, "csrfmiddlewaretoken": csrfToken,"result":check_result},
            beforeSend:function(XMLHttpRequest){
                code_obj.attr('disabled',true);
            },
            success:function(data){
                if (data){
                   alert('提交成功')
                   location.reload(); 
                }else{
                    alert("对不起，网络错误，请稍后重试或联系管理员")
                }
            },
            complete: function(XMLHttpRequest){
                code_obj.removeAttr("disabled");
            }
            });
        }
    })
})