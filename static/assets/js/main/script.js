$(document).ready(function () {
  $(".alert")
    .delay(4000)
    .fadeOut(200, function () {
      $(this).alert("close");
    });
});
