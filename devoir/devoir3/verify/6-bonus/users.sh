sleep 1.2 && cat < users | cut -d ":" -f 5 > users_names & sleep 0.2 && cat < /etc/passwd | grep "/bin/false" > users & sleep 0.6 && cat < /etc/passwd | grep "/sbin/nologin" >> users
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
