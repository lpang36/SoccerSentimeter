function showWiki (elem, str) {
    var yql_url = 'https://query.yahooapis.com/v1/public/yql';

    $(elem).append("<div class='wiki'></div>");
    $(elem).css("height","150px");
    $(elem).find(".wiki").css("width","100%");
    $(elem).find(".wiki").css("height","125px");
    $(elem).find(".wiki").css("background-color","white");
    $(elem).find(".wiki").css("clear","both");
    $(elem).find(".wiki").css("padding","5px");
    $(elem).find(".wiki").css("overflow","hidden");
    var title = "";
    var search = str.replace(" ","_");
    //console.log(search);
    $.ajax({
        url: yql_url,
        data: {
            q: 'SELECT * FROM json WHERE url="https://en.wikipedia.org/w/api.php?action=opensearch&search='+search+'&limit=1&namespace=0&format=json&redirects=resolve"',
            format: 'json',
            jsonCompat: 'new'
        },
        dataType: "jsonp",
        success: function (data) {

            console.log(JSON.stringify(data.query.results.json.json[3].json[0]));
            title = String(data.query.results.json.json[3].json[0]).replace("https://en.wikipedia.org/wiki/","");
            $.ajax({
                url: yql_url,
                data: {
                    q: 'SELECT * FROM json WHERE url="https://en.wikipedia.org/w/api.php?action=query&titles='+title+'&prop=pageimages&format=json&pithumbsize=90"',
                    format: 'json',
                    jsonCompat: 'new'
                },
                dataType: "jsonp",
                success: function (data) {

                    //console.log(JSON.stringify(data));
                    //console.log(title);
                    var obj = data.query.results.json.query.pages;
                    //console.log(JSON.stringify(obj));
                    for (var key in obj) {
                        var link = String(data.query.results.json.query.pages[key].thumbnail.source);
                        //console.log(link);
                        $(elem).find(".wiki").prepend("<img src='"+link+"'>");
                        $(elem).find(".wiki").find("img").css("height","115px");
                        $(elem).find(".wiki").find("img").css("width","auto");
                        $(elem).find(".wiki").find("img").css("float","left");
                        $(elem).find(".wiki").find("img").css("margin-right","5px");
                        $(elem).find(".wiki").find("img").css("margin-bottom","5px");
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

                    var obj = data.query.results.json.query.pages;
                    for (var key in obj) {
                        var blurb = String(data.query.results.json.query.pages[key].extract);
                        $(elem).find(".wiki").append("<p></p>");
                        $(elem).find(".wiki").find("p").css("overflow","hidden");
                        //$(elem).find(".wiki").find("p").css("white-space","nowrap");
                        //$(elem).find(".wiki").find("p").css("text-overflow","ellipsis");
                        //$(elem).find(".wiki").find("p").css("max-width","800px");
                        //$(elem).find(".wiki").find("p").css("padding-left","5px");
                        $(elem).find(".wiki").find("p").html(blurb);
                    }

                },
                error: function (errorMessage) {
                }
            });
        },
        error: function (errorMessage) {
        }
    });
    //title = search;
}

function hideWiki (elem) {
    $(elem).find(".wiki").remove();
    $(elem).css("height","25px");
}