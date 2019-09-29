# Instagram-Bot
A simple python script to follow the followers/following of another person, then unfollow them 
if they don't follow back. The goal is to have a decent following of real people who are somehow related to you - mutual friends, same school, etc.

## Requirements
Install the requirements with 
```
pip install -r requirements.txt
```

## Config File
To run this, create a file called `pw.config`. Within that file, use the following format for your username and password, like in `config.example`:
```
username:<username>
password:<password>
users:['user1', 'user2']
exceptions:['id1', 'id2']
```

## Running the program
`main.py` follows all the followers of `users` in the config file. `unfollow.py` unfollows every account that you follow, that doesn't follow you back, excluding the user IDs mentioned in `exceptions`


