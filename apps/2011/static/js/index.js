/*
    JavaScript for PyCon China Offical Website
    Author: Datong Sun (Dndx)
    Blog: idndx.com
    Version: 2011.11.21
*/
function load_person(year){
    $.get('/static/xml/speakers-2011-' + LANG + '.xml', function(data){
        var $imgs = $(".speakers img")
        $(data).find("speaker").each(function(i, speaker){
            var fullname = $(speaker).children("fullname").text()
            $imgs.each(function(i, e){
                if ($(e).attr('alt') == fullname){
                    var html = ""
                    if ($(speaker).children('nickname').text()){
                        html += '<h4>' + $(speaker).children('nickname').text() + '（' + fullname + '）' + '</h4>'
                    }else{
                        html += '<h4>' + fullname + '</h4>'
                    }
                    html += (LANG.indexOf('en')==-1 ? "<strong>主题：</strong>" : "<strong>Title:</strong>") + $(speaker).children("speech").text() + '<br />'
                    if ($(speaker).children("company").text()){
                        html += (LANG.indexOf('en')==-1 ? '<strong>组织：</strong>' : '<strong>Organization:</strong>') + $(speaker).children("company").text() + '<br />'
                    }
                    if ($(speaker).children("position").text()){
                        html += (LANG.indexOf('en')==-1 ? '<strong>头衔：</strong>' : '<strong>Job:</strong>') + $(speaker).children("position").text() + '<br />'
                    }
                    html += (LANG.indexOf('en')==-1 ? "<strong>简介：</strong>" : "<strong>Description:</strong>") + $(speaker).children("desc").text()
                    html += '<div style="clear:both; "></div>'
                    $(html).insertAfter(e)
                }
            })
        })
    })
}

$(function(){
    $("#hero-selector > div").filter(":first").addClass('active').end()
                             .click(function(){
								  $(":animated").stop(true, true)
                                  var current = $("div.active").text()
                                  var clicked = $(this).text()
                                  var offset = (clicked - current) * 880
                                  $(this).addClass("active").siblings().removeClass("active")
                                  $("#content").animate({"left": "-=" + offset + "px"}, "slow")
								  if (Hero_anim[$(this).attr("id")]){
									  $(document).clearQueue("Animation")
								      Hero_anim[$(this).attr("id")]()
								  }
                              })
	$(".has_sub_schedule").click(function(){
		                       $(this).children('ul').slideDown('slow').end().siblings('.has_sub_schedule').children('ul').slideUp('slow')
		                   })
	
})

$(window).load(function(){
	$("#first").trigger("click")
	
	function nextHero(){
		var total = $("#hero-selector > div:last").text()
		var current = $("#hero-selector > div.active").text()
		if (current < total) {
			$("#hero-selector > div.active + div").trigger('click')
		} else {
			$("#hero-selector > div:first").trigger('click')
		}
	}
	
	setInterval(nextHero,10000)
})

Hero_anim = {
		first: function() {
			$("#first-hero img").css({rotate: "90deg", marginLeft: -50})
			$("#first-hero h1").css({marginRight: -570, opacity: 0})
			$("#first-hero p").css({position: "relative", top: 50, opacity: 0})
			
			var FUNC=[
			function() {$("#first-hero img").animate({rotate: "0deg", marginLeft: 0}, 1000, aniCB);},
			function() {$("#first-hero h1").animate({marginRight: 0, opacity: 1}, 1500, aniCB);},
			function() {$("#first-hero p").animate({top: 0, opacity: 1}, 1500, aniCB);}
			];
			var aniCB=function() {
				$(document).dequeue("Animation");
			}
			$(document).queue("Animation",FUNC);
			aniCB()
	     },
		third: function(){
			$("#third-hero .span4").css({position: "relative", left: -50, opacity: 0})
			$("#third-hero .span11 > *").css({position: "relative", top: 50, opacity: 0})
			
			var FUNC=[
			function() {$("#third-hero .span4").animate({left: 0, opacity: 1}, 1000, aniCB);}
			];
			
			$("#third-hero .span11 > *").each(function(e){
													var $this = $(this)
													FUNC.push( function(){$this.animate({top: 0, opacity: 1}, 500, aniCB);} )
				                             })
			
			var aniCB=function() {
				$(document).dequeue("Animation");
			}
			$(document).queue("Animation",FUNC);
			aniCB()
		 },
		 forth: function(){
			$("#forth-hero .span-one-third").css({position: "relative", top: -300, opacity: 0})
			$("#forth-hero .span8").css({position: "relative", top: 300, opacity: 0})
			
			$("#forth-hero .span-one-third").animate({top: 0, opacity: 1}, 1000)
			$("#forth-hero .span8").animate({top: 0, opacity: 1}, 1000)
		 },
		 second: function() {
			$("#second-hero img").css({opacity: 0})
			$("#second-hero h2").css({marginRight: -570, opacity: 0})
			$("#second-hero p").css({position: "relative", top: 50, opacity: 0})

			$("#second-hero img").animate({opacity: 1}, 3000)
			var FUNC=[
			function() {$("#second-hero h2").animate({marginRight: 0, opacity: 1}, 1500, aniCB);},
			function() {$("#second-hero p").animate({top: 0, opacity: 1}, 1500, aniCB);}
			];
			var aniCB=function() {
				$(document).dequeue("Animation");
			}
			$(document).queue("Animation",FUNC);
			aniCB()
	     }
}