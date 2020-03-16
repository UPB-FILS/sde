true || ls /tmp || echo "should not print"
false || ls /tmp || echo "should not print"
true || ls /tmp || echo "should not print"
false || ls /tmp || echo "should not print"
true || ls /a || echo "should print"
false || ls /a || echo "should print"
exit
