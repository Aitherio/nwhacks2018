#Hardcode strings
##i.e. goodbye_message = "Okay, maybe tomorrow! Have a splenda day!"

def lambda_handler(event, context):

    name = event["currentIntent"]["slots"]["Name"].title()
    response = {
                "dialogAction":
                    {
                    "fulfillmentState":"Fulfilled",
                    "type":"Close","message":
                        {
                        "contentType":"PlainText",
                        "content": "Hi "+name+", good to see you! I'm Tim, the coffee runner! I'm here to help you be the best person in the office - or, the best coffee fetcher your office has ever seen. Are you going on a coffee run today?"
                        }
                    }
                }
    return response
#Add buttons to the above function - "Yes!"" & "Not Today" for the user to input their answer
#Pseudo-Code Follows:
## if "yes!", launch CoffeeShop intent then CoffeeTime intent;
#   Ask User for the Channel that they want to grab coffee for
#  Ref: use drop down menus https://api.slack.com/docs/message-menus

## if "not today", say goodbye message
    
#Slash Command Integration with /coffeerun to initiate app


#Channel name maps to the Channel ID [channels.id] maps to the members list [channels.members]
##Ref: https://api.slack.com/methods/channels.list

#Message sent to each member [channels.members], store member's coffee order
cream = params['cream']
sugar = params['sugar']

return respond(None, "Your coffee with %i cream and %i sugar is on its way!" % (cream, sugar))

#Sorting Coffee Order

#Coffee Order Sent back to Original Runner
