# ghostpost
Author: Chris Wilson
Worked on it with Sean and Koren.
The GhostPost Machine™ is a website where people can anonymously post Boasts or Roasts of whatever they want. Like most services, there is a character limit: 280 characters. We are deliberately not dealing with logins, as that is outside the scope of the project (and beyond our time constraints). 

A front end is necessary to make this work, though it doesn't have to be pretty -- invest as much time as you want into it (assuming your application already has the requested features 🤓).
Your Task
Create a Django application with the following features.

Back end:

One model to represent both boasts and roasts
Boolean to tell whether it's a boast or a roast
CharField to put the content of the post in
IntegerField for up votes
IntegerField for down votes
DateTimeField for submission time

Front end: 
Homepage that displays boasts and roasts, sorted by time submitted (hint --> https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by (Links to an external site.)Links to an external site.)
Buttons to filter the content by either boasts or roasts, sorted by time submitted
Upvote and downvote buttons for each boast and roast
when clicked, these buttons affect the numbers on the relevant post appropriately
Ability to sort content based on vote score (hint: you may need to calculate the vote score) 
Page to submit a boast or a roast

Hints:
button hrefs can use template data, just like everything else
voting is not meant to be secure; this is effectively a proof of concept application
you do not need to worry about figuring out if someone has already voted on something
 