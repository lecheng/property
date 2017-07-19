$("#edit-btn").click(function(){
    $("#edit-panel").removeClass("hide");
    $("#info-panel").hide();
    $("ol").append("<li><a href='#' class='active'>经纪人信息编辑</a></li>")
})
$("#cancel-btn").click(function () {
    $("#edit-panel").addClass("hide");
    $("#info-panel").show();
    $("ol li:last-child").remove()
})
var count = 0;
$("#edit-panel input").each(function(){
    if(count == 0)  this.value = $("h4:first").text();
    else if(count == ($("#edit-panel input").length-1));
    else    this.value = $("#info-panel .item")[count-1].textContent.trim().substr(2);
    count++;
})

$("#qrcode-submit").click(function(){
    $("#qrcode-form").submit();
})