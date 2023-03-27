# Day 072 Challenge

Now that we know about secure passwords, we can really protect our diary program.

Go back 10 days and grab your diary code from Day 62.

When you have it, add the following features:

1. The first time the diary is run, the user must create a username and password.
1. Salt & hash the password and store it in the database with the username as the key.
1. Then proceed to the diary.
1. The next time that program is run, it should prompt for the username and password, and only allow access if they are correct.
1. The username, password, and salt should be excluded from diary entry outputs, for obvious reasons.
