# Hydratation Bot :droplet:
A very simple script to remind your team to stay hydrated when hot outside.

## Getting Started
The script is based on OpenWeather API and Slack WebHook
</br>Create a WebHook in your slack application.
</br>Set the `.env` file.
</br>Then run:

```zsh
python3 hydratation_bot/main.py
```
The script will check the outside temp every 4 hours and post a slack message if it's too hot.
</br>Please Drink responsibly