<!DOCTYPE html>
<html>
 <head>
  <title>HELLO WORLD</title>
 </head>
 <body>
  <p>Hello <?= (isset($_GET['subject']) ? htmlentities($_GET['subject']) : 'World'); ?></p> 
 </body>
</html>
