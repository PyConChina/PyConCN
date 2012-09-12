/*
    JavaScript for PyCon China Offical Website
    Author: Datong Sun (Dndx)
    Blog: idndx.com
    Version: 2011.11.21
*/
$(function(){
	$.get('/static/xml/speakers-2011-' + LANG + '.xml', function(data){
		speakers = data
		var $tds = $("tr td:nth-child(3)")
		$(data).find("speaker").each(function(i, e){
			var fullname = $(e).children("fullname").text()
			$tds.each(function(i, e){
				if ($(e).text().indexOf(fullname) != -1){
					$(e).addClass("desc")
				}
			})
		})
	})
	$('td.desc').popover({title: function(){return $(this).text()}, content: function(){
		var tip = ""
		var hovername = $(this).text()
		$(speakers).find("speaker").each(function(i, e){
			if (hovername == $(e).children("fullname").text()){
				if ($(this).children("avatar").text()){
					tip += '<img src="http://pycon.b0.upaiyun.com/images/speakers/' + $(this).children("avatar").text() + '" alt="' + $(this).children("fullname").text() + '" />'
				}else{
					tip += '<img src="http://pycon.b0.upaiyun.com/images/speakers/nopic.gif" alt="' + $(this).children("fullname").text() + '" />'
				}
				if ($(this).children("company").text()){
				    tip += (LANG.indexOf('en')==-1 ? "<strong>组织：</strong>" : "<strong>Organization:</strong>") + $(this).children("company").text() + '<br />'
				}
				if ($(this).children("position").text()){
					tip += (LANG.indexOf('en')==-1 ? "<strong>头衔：</strong>" : "<strong>Job:</strong>") + $(this).children("position").text() + '<br />'
				}
				tip += (LANG.indexOf('en')==-1 ? "<strong>简介：</strong>" : "<strong>Description:</strong>") + $(this).children("desc").text()
				tip += '<div style="clear:both; "></div>'
			}
		})
		return tip
    }, html:true, live:true})
})