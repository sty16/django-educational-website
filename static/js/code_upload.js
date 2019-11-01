$(function(){
    $('#CodeUploadBtn').click(function(){
        var formdata = new FormData($('#code_form')[0])
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
                alert('文件上传成功')
            },
            success: function(result) {
                $('html').html(result)
            }
        });
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
                if (data.status =="success"){
                    location.href = '/media/' + data.FilePath;
                    var count_obj = $('i#' + id);
                    console.log(count_obj)
                    count_obj[0].textContent = (parseInt(count_obj[0].textContent) + 1).toString();
                }else{
                    // window.location.href = '/media/' + data.FilePath;
                    alert("对不起，网络错误，请稍后重试或联系管理员")
                }
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
