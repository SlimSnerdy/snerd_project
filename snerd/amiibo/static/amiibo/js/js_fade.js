$(document).ready(function() {
  $("img").hover(function() {
    $(this).stop().animate({opacity: "0.8"}, 'fast');
  },
  function() {
    $(this).stop().animate({opacity: "1"}, 'fast');
  });
});