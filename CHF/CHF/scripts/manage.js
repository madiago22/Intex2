/**
 * Created by Carter on 2/1/2015.
 */
$('.archiveBtn').click(function(){
   if(window.confirm("Are you sure you want to archive this record?"))
       $('form').submit();
});