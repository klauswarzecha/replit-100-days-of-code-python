# Day 071 Challenge

Today's challenge is to build a simple login system.

Your program should:

1. Display a menu with the ability to add a user or login.
1. 'Add' user should:
    1. Ask for a username and password.
    1. Create a new password and a randomly generated 4 digit salt.
    1. Append the salt to the password and hash it.
    1. Store the hash and the salt in a repl db with the username as the key.
1. 'Login' should:
    1. Get username and password input.
    1. Display a success message if details are correct.
1. This system should work with multiple users.