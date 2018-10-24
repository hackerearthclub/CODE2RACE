<?php
date_default_timezone_set('UTC');
?>
<script>
var d = new Date(<?php echo time() * 1000 ?>);
function digitalClock() {
  d.setTime(d.getTime() + 1000);
  var hrs = d.getHours();
  var mins = d.getMinutes();
  var secs = d.getSeconds();
  mins = (mins < 10 ? "0" : "") + mins;
  secs = (secs < 10 ? "0" : "") + secs;
  var apm = (hrs < 12) ? "am" : "pm";
  hrs = (hrs > 12) ? hrs - 12 : hrs;
  hrs = (hrs == 0) ? 12 : hrs;
  var ctime = hrs + ":" + mins + ":" + secs + " " + apm;
  document.getElementById("clock").firstChild.nodeValue = ctime;
}
window.onload = function() {
  digitalClock();
  setInterval('digitalClock()', 1000);
}
</script>
<div id="clock"> </div>
