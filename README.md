# local-chat-messenger

## Usage

1. Start the server

```bash
python3 server.py
```

2. Start the client

```bash
python3 client.py
```

3. Input a message
Enter name or address, and the corresponding Faker data (name or address) will be automatically generated and returned from the server to the client.
If any other message is entered, a random country name will be generated and returned.

4. Customization
If you want to return data corresponding to other inputs, add new key-value pairs to the dict variable in server.py.

5. Configuration
Common settings used by both the client and server are summarized in config.json. Please add any necessary configurations according to your needs.
