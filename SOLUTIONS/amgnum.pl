print "enter a num:";
$n = <stdin>;
$t = $n;
$sum=0;

while($n!=0)
{
$rem = $n %10;
$sum = $sum + $rem*$rem*$rem;
$n=$n/10;
}

if($t==$sum)
{
print "yes";
}
else
{
print "no";
}
