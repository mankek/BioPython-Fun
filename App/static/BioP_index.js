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
        var content = preview[0][name]
        var id = content["id"]
        var description = content["description"]
        var seq_length = content["Sequence length"]
        var features = content["features"]
        var source = content["from"]
        alert("Id: " + String(id) + "\nDescription: " + String(description) +
        "\nSequence Length: " + String(seq_length) + "\nFeatures: " + String(features) + "\nSource: " + String(source))
//        var myWindow = window.open("", "MsgWindow");
//        myWindow.document.writeln("<b>The result is as follows:</b>")
//        myWindow.document.write(String(preview))
        location.replace("http://127.0.0.1:5000/");
    }
})

