import requests

print(
    requests.get(
        "https://cdn.clawroyale.ai/api/version"
    ).text
)
