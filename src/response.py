def respond(msg, attack, config):
    if not config["enable_response"]:
        return

    if attack:
        print(f"Blocking CAN ID: {msg['id']}")