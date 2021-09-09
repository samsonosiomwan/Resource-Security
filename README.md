

## Secure a Resource

## User Story
You just resumed after a 3 weeks leave, you met most of the company's employees from different departments talking about the company’s data that was breached. You quickly ran into the directors office to get the detailed context of what happened. The director affirmed the incident that the company's most valuable resource and business logic has been sold out to our competitor.

As the most senior engineer the company has, the director wants you to secure the resources and only allow admin and super admin to view and access it.

Luckily for us the company already has a database where all the employee records are stored, an authentication function that authenticates users and a function that returns the company's most valuable resource.

Since the company software has already been built, tested and deployed. It is not advisable to manually change or alter all these implementations and modules that can lead to re-writing the whole codebase which we would not want to do and also to follow Open/Close principles that says software should Open for Extension but Close for modification.

In this task you are to write a decorator function that will secure the company’s most valuable resources and also logs all employee information that access or tried to access the resource
These are the detailed specifications of what the company wants

- Only user with admin and super admin role should be able to to view the resource
- Logs admin and super admin information to a file named `access_granted.txt`. The information to be logged are full name, role, date, time e.g `Admin Oluwatosin Ayodele viewed company resources on 1/4/2021 at 10:30`
- All other employee should not have access to the resource
- Return a warning message to all other employees who attempt to access the resource `You are not allowed to view this resource`
- Logs other employees details to a file named `access_denied.txt` with the following information full name, role, date, time e.g `Marketer Favour Nnabue tried to view company most valuable resources on 10/4/2021 at 10:30`
- If the resource was tried to be accessed by an anonymous user return a message that reads `Only staff can access this resource`

Note: The time and date should be current time the user access or tried to access the resource.

## How to use this app
- clone the this repo
- goto resource.py which is the entry point of this application
- run the application by pressing the play button on the or use command R for mac users
- to test the this use cases , open resource.py and change the email to a correct staff mail in db.py
- to test for not a staff use the dafualt email or use any imaginary mail