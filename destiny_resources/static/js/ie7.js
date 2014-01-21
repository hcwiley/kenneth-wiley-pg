$(window).ready(function(){
  $('form button').click(function(){
    $(this).closest('form').submit();
  });
});
