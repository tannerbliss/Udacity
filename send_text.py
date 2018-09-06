from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcdb799bb9bee8505fdfd014aa550e78b"
# Your Auth Token from twilio.com/console
auth_token  = "a7c215afbef5c2d6a449acdcd2707102"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14049198597",
    from_="+14046490689",
    body="I am ALWAYS watching you......")

print(message.sid)
