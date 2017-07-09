function showWiki (elem, str) {
    var yql_url = 'https://query.yahooapis.com/v1/public/yql';

    $(elem).append("<div class='wiki'></div>");
    $(elem).css("height","125px");
    $(elem).find(".wiki").css("width","100%");
    $(elem).find(".wiki").css("height","100px");
    $(elem).find(".wiki").css("background-color","white");
    $(elem).find(".wiki").css("clear","both");
    $(elem).find(".wiki").css("padding","5px");
    var title = "";
    var search = str.replace(" ","_");
    console.log(search);
    $.ajax({
        url: yql_url,
        data: {
            q: 'SELECT * FROM json WHERE url="https://en.wikipedia.org/w/api.php?action=opensearch&search='+search+'&limit=1&namespace=0&format=json"',
            format: 'json',
            jsonCompat: 'new'
        },
        dataType: "jsonp",
        success: function (data) {

            console.log(JSON.stringify(data));
            title = String(data[3]).replace("https://en.wikipedia.org/wiki/","");

        },
        error: function (errorMessage) {
        }
    });
    console.log(title);
    $.ajax({
        url: yql_url,
        data: {
            q: 'SELECT * FROM json WHERE url="https://en.wikipedia.org/w/api.php?action=query&titles='+title+'&prop=pageimages&format=json"',
            format: 'json',
            jsonCompat: 'new'
        },
        dataType: "jsonp",
        success: function (data) {

            console.log(JSON.stringify(data));
            var obj = data.query.pages;
            for (var key in obj) {
                var link = String(data.query.pages[key].thumbnail.source);
                $(elem).find(".wiki").append("<img src='"+link+"'");
                $(elem).find(".wiki").find("img").css("height","90px");
                $(elem).find(".wiki").find("img").css("width","auto");
            }

        },
        error: function (errorMessage) {
        }
    });
    $.ajax({
        url: yql_url,
        data: {
            q: 'SELECT * FROM json WHERE url="https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=&explaintext=&titles='+title+'"',
            format: 'json',
            jsonCompat: 'new'
        },
        dataType: "jsonp",
        success: function (data) {

            var obj = data.query.pages;
            for (var key in obj) {
                var blurb = String(data.query.pages[key].extract);
                $(elem).find(".wiki").html(blurb);
            }

        },
        error: function (errorMessage) {
        }
    });
}

function hideWiki (elem) {
    //$(elem).find(".wiki").remove();
    //$(elem).css("height","25px");
}