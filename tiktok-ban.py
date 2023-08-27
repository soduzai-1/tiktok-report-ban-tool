import requests

# Set up your TikTok API credentials
api_url = 'https://api.tiktok.com'
access_token = 'your_access_token'

# Get user input for the username and report reason
username = input("Enter the username you want to report: ")
report_reason = input("Enter the reason for reporting: ")

# Create a function to report a user
def report_user(username, reason):
    endpoint = f'/v2/users/@{username}/report/'
    params = {
        'access_token': access_token,
        'reason': reason
    }
    
    try:
        response = requests.post(api_url + endpoint, params=params)
        if response.status_code == 200:
            print(f"Successfully reported {username}.")
        else:
            print(f"Error reporting {username}.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

# Report the user
report_user(username, report_reason)
