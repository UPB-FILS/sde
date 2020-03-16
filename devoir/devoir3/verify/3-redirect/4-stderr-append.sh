ls /inexistent 2> test.err
ls /notexistent 2>> test.err
cat test.err
exit
