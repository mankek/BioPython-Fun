$(document).ready(function(){
    $("#query_btn").click(function(){
        $("#query").show();
        $("#upload").hide();
    });

    $("#upload_btn").click(function(){
        $("#upload").show();
        $("#query").hide();
    });

    $(":radio").click(function(){
        if ($("#nuccore").prop("checked")) {
            $("#type").attr("list", "Nucleotide")
        }
    })
})

