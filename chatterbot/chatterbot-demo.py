#!/usr/bin/env python3
# reference: https://medium.com/@guandika8/on-your-local-pc-a-local-chatbot-that-is-completely-offline-and-private-26b298dc4076

from chatterbot import ChatBot

bob = ChatBot(
  "Bob",
  logic_adapters=[
    "chatterbot.logic.BestMatch",
	"chatterbot.logic.TimeLogicAdapter"
  ]
)

while True:
  user_input = input("You: ")
  
  if (user_input.lower() in ["bye", "exit"]):
    print("Bob: Good bye!")
    break
  
  response = bob.get_response(user_input)

  print("Bob: ", str(response))
  
