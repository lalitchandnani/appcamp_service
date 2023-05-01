import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AppCampSetting

@api_view(['POST'])
def notify_request(request):
    name = request.data.get('name')
    email = request.data.get('email')
    subdomain = request.data.get('subdomain')
    subject = 'AppCamp subdomain request recieved'
    body = "Recieved a new Subdomain request from %(name)s(%(email)s) for subdomain: %(subdomain)s" % \
                {"name": name, "email": email, "subdomain": subdomain};
    
    # Your SendGrid API key
    api_key = AppCampSetting.objects.first().sendgrid_api_key
    # Request headers
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    to_email = AppCampSetting.objects.first().sender_email
    sender_email = AppCampSetting.objects.first().recipient_email
    # Request body
    data = {
        'subject': subject,
        'sender': { "name": "AppCamp", "email": sender_email },
        'type': "classic",
        'htmlContent': body,
        'to': [{ 
            "email": to_email
        }]
    }

    # API endpoint
    url = 'https://api.sendinblue.com/v3/smtp/email'

    # print(headers)
    # print(data)
    # print(url)

    # Make the API call
    response = requests.post(url, headers=headers, json=data)

    # Print the response status code and body
    # print('Status code:', response.status_code)
    # print('Response body:', response.json())
    response_data = {'success': True }
    return Response(response_data)
