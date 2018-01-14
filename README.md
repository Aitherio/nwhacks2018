# nwhacks2018
NWHacks 2018 Hackathon Jan 13-14 https://devpost.com/software/coffee-runner

## Coffee Runner chatbot using AWS and Slack API

This is a chatbot that allows a user who is going on a coffee run to grab everyone's order into a list without the user phyiscally needing to ask the others what they want, let the bot do the work.

Although it is currently a WIP (yes even though its after the hackathon) we have learned a lot about the chatbot framework despite that none of us have ever touched it before.

Check it out at http://coffeerunner.tech!

## Team

* [Monica](https://github.com/bui1) - *Setting up backend service with Lambda Amazon function*
* [Amy](https://github.com/AmyHong0502) - *Working and testing with database and backend*
* [Merina](https://github.com/merinaleong) - *Design of the application*
* [Serena](https://github.com/coriils) - *Setting up frontend service and connecting app to Slack*
* [Cameron](https://github.com/aitherio) - *Setting up frontend service with main commands and intents*


## Resources for future use
* https://chatbotslife.com/write-a-serverless-slack-chat-bot-using-aws-e2d2432c380e
* https://medium.com/@srinivasanchandramouli/noobs-guide-to-building-a-chatbot-using-lex-54c88b5323ea
* https://aws.amazon.com/blogs/machine-learning/building-better-bots/
* https://www.fullstackpython.com/blog/aws-lambda-python-3-6.html
* https://medium.com/@vikrame/build-a-chatbot-using-amazon-lex-and-aws-lambda-b90c75ea6626


## Inspiration
The original idea was to create a Slack chatbot that logged your daily mood and events. However, Slack is primarily for teams and we needed to find a use case that was useful and different from the already long list of published apps. In the hours leading up to midnight, Monica and Amy continued to work on setting up Amazon Lambda and Amazon Lex while Cameron and Serena brainstormed use cases that we would use ourselves. Pulling from previous work experience, we gravitated towards a bot that would assist in compiling orders for coffee runs. However, it would live solely on the private bot channel to avoid two distracting app pitfalls.
* 1. Having too many group chats on Slack that are not for work teams
* 2. Large coffee run channel may be a distraction and open up the offer to too large of an audience
