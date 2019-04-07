var news = {
        newsLocation: '.news',
        newsItems: [],
        updateInterval: config.news.interval || 5500,
        fadeInterval: 2000,
        intervalId: null,
};


news.init = function () {
    $.ajax({
        url: "/news",
        type: "GET",
        dataType: "json",
        success: function (data) {
            console.log(data);
            news.newsItems = data;
        }
    });

    let i = 0;
	this.intervalId = setInterval(function () {
        $(this.newsLocation).updateWithText(news.newsItems[i++], this.fadeInterval);
        console.log(news.newsItems[i]);
        if(typeof (news.newsItems[i]) == "undefined"){
            i = 0;
        }
	}.bind(this), this.updateInterval);
};