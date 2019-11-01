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
            }
        });
    })
});