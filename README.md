# Bitcoin Price Notification

To run this program first clone the directory and run the commands in terminal

```Bash
pip install -r 'requrirements.txt'
```

Once the required packages are installed, we need to create accounts (FREE) at [Coinmarketcap](https://pro.coinmarketcap.com/login/) and [IFTTT](https://ifttt.com/join) to get the api keys.

To create webhooks: follow the steps

Once you haved logged into IFTTT website:

To create a new test applet follow these steps:

1. Click on the big “this” button

2. Search for the “webhooks” service and select the “Receive a web request” trigger
3. Let’s name the event `bitcoin_price_emergency`
4. Now select the big “that” button
5. Search for the “notifications” service and select the “Send a rich notification from the IFTTT app” action
6. Give it a title, like “Bitcoin price emergency!”
7. Set the message to Bitcoin price is at ${{Value1}}. Buy or sell now!

Create the action and finish setting up the applet

> To recieve notifications on your phone you also need to install IFTTT application and login with the same e-mail you created the IFTTT account.

Now the we have our API keys, lets finish this up quickly

```BASH
touch .env
```

Inside `.env` file, enter the api keys

```Bash
export API_KEY={coinmarketcap-api}
export  IFTTT_KEY={IFTTT-api}
```

and save (ofcourse).

> Also, in `crypto_price.py`, you might want to updatae

> And then finally,

run

```Bash
pyhton3 crypto_price.py
```

Thats it!!

> If stuck somewhere, feel free to ping me!
