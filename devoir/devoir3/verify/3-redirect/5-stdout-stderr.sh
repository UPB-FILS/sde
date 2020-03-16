echo "int main () {printf (300); return 0;}" > test.c
gcc -S -o test.c  > test.out 2> test.err
rm test.c
echo "Output"
cat test.out
echo "Error"
cat test.err
exit
