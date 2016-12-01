// Code goes here


$(document).ready(function() {
  $(".productitem").hover(function(){
      $(".edition-logo", this).stop().animate({
        opacity: "show",
        bottom: "0",
        height: "100%"
        },
        400,
        function() {
    // Animation complete.
    });

    $(".edition-logo a + a", this).stop().fadeIn("slow", "linear");



  }, function() {
    $(".edition-logo", this).stop().animate({
        opacity: "show",
        bottom: "-30",
        height: "100%"
        },
        400,
        function() {
    // Animation complete.
    });

        $(".edition-logo a + a", this).stop().fadeOut("slow", "linear");


  });

});