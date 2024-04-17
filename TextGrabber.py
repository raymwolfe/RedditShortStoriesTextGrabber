import praw  # Import the praw library, which is a Python wrapper for the Reddit API

# Replace with your Reddit client ID and secret
client_id = "YOUR_CLIENT_ID"  # Replace this with your Reddit client ID
client_secret = "YOUR_CLIENT_SECRET"  # Replace this with your Reddit client secret

# Replace with the subreddit name
subreddit_name = "your_subreddit"  # Replace this with the name of the subreddit you want to analyze

# Create a Reddit instance with the provided client ID, client secret, and a user agent
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent="your_script_name")

# Access the specified subreddit
subreddit = reddit.subreddit(subreddit_name)

# Loop through the hot posts in the subreddit, limiting to 1 post
for submission in subreddit.hot(limit=1):
    top_comment = None  # Initialize a variable to store the top comment
    top_comment_author = None  # Initialize a variable to store the author of the top comment
    # Loop through the comments of the current submission, sorted by 'top', and limiting to 1 comment
    for comment in submission.comments.sort('top', limit=1):
        # Check if there is no top comment yet or if the current comment has a higher score than the current top comment
        if top_comment is None or comment.score > top_comment.score:
            top_comment = comment  # Set the current comment as the new top comment
            top_comment_author = comment.author  # Set the author of the current comment as the top comment author

    # Check if a top comment was found
    if top_comment:
        # Print the title of the post
        print(f"Post Title: {submission.title}")
        # Print the score of the top comment
        print(f"Top Comment Score: {top_comment.score}")
        # Print the text of the top comment
        print(f"Top Comment Text: {top_comment.body}")
        # Print the author of the top comment
        print(f"Top Comment Author: {top_comment_author}")
        break  # Exit the loop after finding the top comment from the first post

# If no posts were found or no top comment was available, print a message
print("No posts found or no top comment available.")