/*
    JavaScript for PyCon China Offical Website
    Author: Datong Sun (Dndx)
    Blog: idndx.com
    Version: 2011.10.16
*/

$(function(){
	$(':button').click(function(){
		var url = "";
		url += "http://ditu.google.cn/maps?";
		url += "f=d&";
		url += "source=s_d&";
		url += "saddr=" + $(":input").val() + "&";
		url += "daddr=" + encodeURI("上海虹口区广纪路838号") + "&";
		url += "hl=zh-CN&";
		url += "geocode=&";
		url += "mra=cc&";
		url += "sspn=0.105738,0.153809&";
		url += "ie=UTF8&";
		url += "z=13&";
		url += "brcurrent=3,0x35b264c8bb78a883:0x6e625b27913261fe%3B5,0&";
		if ($(this).val() == "驾车") {
			url += "noexp=0&";
			url += "noal=0&";
			url += "sort=time";
		}
		if ($(this).val() == "公交") {
			url += "dirflg=r&";
			url += "start=0";
		}
		window.open(url)
	})
})