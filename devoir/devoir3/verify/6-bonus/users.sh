cat < /etc/passwd | grep "/bin/false" > users && cat < /etc/passwd | grep "/sbin/nologin" >> users && cat < users | cut -d ":" -f 5 > users_names
sleep 1.7
echo "Users"
cat users
cat users_names > users
echo "Users"
cat users
rm users_names; rm users
ls users_names || echo "no users_names file"
ls users || echo "no users file"
exit