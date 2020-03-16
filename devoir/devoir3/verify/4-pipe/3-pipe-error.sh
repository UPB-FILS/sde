echo "int main () {printf (300); return 0;}" > test.c
gcc -S -o test.c | sort
rm test.c
exit

