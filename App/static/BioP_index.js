$(document).ready(function(){
    $("#query_btn").click(function(){
        if ($("#query").css("display") != "block") {
            $("#query").show();
            $("#chart").hide();
            $("#upload").hide();
            $("#help").hide();
        }
    });

    $("#upload_btn").click(function(){
        if ($("#upload").css("display") != "block") {
            $("#upload").show();
            $("#chart").hide();
            $("#query").hide();
            $("#help").hide();
        }
    });

    $("#help_btn").click(function(){
        if ($("#help").css("display") != "block") {
            $("#help").show();
            $("#chart").hide();
            $("#upload").hide();
            $("#query").hide();
        }
    })

    $("#chart_btn").click(function(){
        if ($("#chart").css("display") != "block") {
            $("#chart").show();
            $("#help").hide();
            $("#upload").hide();
            $("#query").hide();
        }
    })

    function openForm(evt, formname){
        formcontent = $(".formcontent");
        for (i = 0; i < formcontent.length; i++) {
            formcontent[i].css("display", "none")
        }
        formlinks = $(".tab")
        for (i = 0; i < formlinks.length; i++) {
            formlinks[i].attr("className", "")
        }

    }

    $("input.radio_q").click(function(){
        if ($("#nuccore").prop("checked")) {
            $("#type").prop("disabled", false)
            $("#type").attr("list", "Nucleotide_list")
        }else if ($("#protein").prop("checked")) {
            $("#type").prop("disabled", false)
            $("#type").attr("list", "Protein_list")
        }
    })

    $("input.radio_c").click(function(){
        if ($(this).prop("checked")){
            $("#filename").prop("value", $(this).attr("id"))
            $("#filetype").prop("value", file_dict[$(this).attr("id")]["rettype"])
            if ($(this).prop("value") == "Nucleotide"){
                $("#charts").prop("disabled", false)
                $("#charts").attr("list", "nucleotide_chart_list")
            } else if ($(this).prop("value") == "Protein") {
                $("#charts").prop("disabled", false)
                $("#charts").attr("list", "protein_chart_list")
            } else {
                alert("No database for file")
            }
        }

    })

    if (preview != "None") {
        var myWindow = window.open("", "MsgWindow");
        myWindow.document.writeln("<b>The result is as follows:</b>")
        myWindow.document.write(String(preview))
        location.replace("http://127.0.0.1:5000/");
    }
})

