/**
 * Created by Carter on 1/21/2015.
 */
var activeCard = $("#homeScreen");
$(document).ready(function(){
 $('.remove-icon').parent().hide();

});
$('.navbar li:has(ul)').hover(function(){
    $(this).find('> ul').stop().slideToggle(400);
});
var login = $('.loginBtn');

login.click(function(){

    $('#wrapper').fadeTo(500,.50);
     $('.remove-icon').parent().fadeIn();
});

$('.remove-icon').click(function(){

    $('.remove-icon').parent().fadeOut();
    console.log($('.remove-icon').parent().get(0).id);
    if($('.remove-icon').parent().get(0).id ="loginPage"){
        $('#wrapper').fadeTo(500,1);
    }
});



//Global functions go here
/*
	Fading Screen function
	Add the .screenNav class to each of the buttons you want to have navigate
	Add an ID to each button that is descriptive of where it points to
	Add that same ID with "Screen" appended to it to the hidden element you
	wish to have shown in place of the current one
*/
$(".screenNav").click(function(){

	var clickedBtn = this.id;
	activeCard.fadeToggle(500,function(){
		activeCard = $("#"+clickedBtn+"Screen");
		activeCard.fadeToggle()
		});
});