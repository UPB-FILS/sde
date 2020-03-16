echo "int main () {printf (300); return 0;}" > test.c
gcc -S -o- test.c &> test.output
rm test.c
echo "Output"
cat test.output
exit
