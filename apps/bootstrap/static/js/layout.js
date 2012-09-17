/*
    JavaScript for PyCon China Offical Website
    Author: Datong Sun (Dndx)
    Blog: idndx.com
    Version: 2011.10.12
*/
$(function(){
    $(".alert-message").alert()
	$(".dropdown-toggle").dropdown()
	
	$('ul.dropdown-menu a').click(function(){
		$.cookie('uliweb_language', $(this).attr('class'), { expires: 7, path: '/' })
		window.location.reload()
	})
})