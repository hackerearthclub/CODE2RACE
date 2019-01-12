print "enter a no:";
$num = <stdin>;
$i = 0;

$c = 0;
$a = 0;
$b = 1;

while($i < $num)
{

print $a." ";
$c = $a+$b;
$a = $b;
$b = $c;
$i++;

}