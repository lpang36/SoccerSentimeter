function toggle (str) {
    if ($("#"+str).css("display") === "block") {
        $("#"+str).css("cssText","display: none!important");
    } else {
        $("#"+str).css("cssText","display: block!important");
    }
}