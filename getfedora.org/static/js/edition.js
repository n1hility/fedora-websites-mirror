// Code goes here


$(document).ready(function() {
  $(".productitem").hover(function(){
      $(".edition-logo", this).animate({
        opacity: "show",
        bottom: "0",
        height: "100%"
        },
        500,
        function() {
    // Animation complete.
    });

    $(".edition-logo a + a", this).fadeIn("slow", "linear");



  }, function() {
    $(".edition-logo", this).animate({
        opacity: "show",
        bottom: "-30",
        height: "100%"
        },
        500,
        function() {
    // Animation complete.
    });

        $(".edition-logo a + a", this).fadeOut("slow", "linear");


  });

});