var config = {
    lang: 'zh_cn',
    time: {
        timeFormat: 12,
        displaySeconds: true,
        digitFade: false,
    },
    weather: {
        //change weather params here:
        //units: metric or imperial
        interval: 120000,
        fadeInterval: 10000,
        params: {
            q: 'raoping',
            units: 'metric',
            // if you want a different lang for the weather that what is set above, change it here
            lang: 'zh_cn',
            APPID: '1e2f64c7e931bfd70166dea3afd5595c'
        }
    },
    tem_hum: {
      mqttServer: 'mqtt.hellowk.cc',
      mqttServerPort: 9001,
      mqttclientName: "magic_mirror_tem_hum",
      temperatureTopic: 'homekit/himitsu/temperature',
      humidityTopic: 'homekit/himitsu/humidity',
      heatIndexTopic: 'homekit/himitsu/heatIndex'
    },
    compliments: {
        interval: 30000,
        fadeInterval: 4000,
        morning: [
            '早上好！',
            '新的一天开始了',
            '睡得还好吗'
        ],
        afternoon: [
            '嗨，你好吗',
            '你看起来很精神',
            '今天看起来不错！'
        ],
        evening: [
            '晚上好',
            '今天过得如何？',
            '晚安，好梦'
        ]
    },
    calendar: {
        maximumEntries: 10, // Total Maximum Entries
		displaySymbol: true,
		defaultSymbol: 'calendar', // Fontawsome Symbol see http://fontawesome.io/cheatsheet/
        urls: [
		{
			symbol: 'calendar-plus-o',
			url: ''
		},
		// {
		// 	symbol: 'soccer-ball-o',
		// 	url: 'https://www.google.com/calendar/ical/akvbisn5iha43idv0ktdalnor4%40group.calendar.google.com/public/basic.ics',
		// },
		// {
			// symbol: 'mars',
			// url: "https://server/url/to/his.ics",
		// },
		// {
			// symbol: 'venus',
			// url: "https://server/url/to/hers.ics",
		// },
		// {
			// symbol: 'venus-mars',
			// url: "https://server/url/to/theirs.ics",
		// },
		]
    },
    news: {
        feed: 'http://www.ftchinese.com/rss/news'
    }
}
