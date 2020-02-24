from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests

from .serializers import CreateUserSerializer

# DOMAIN = dev-c-nmilr5.auth0.com
CLIENT_ID = 'T959p70EB2bKnjsDnqgIyJKkScj4iKMsFKCUScc9'
CLIENT_SECRET = 'pcGirJlNw285vyvEPwdMnkhC0dJZmVmZAg6g9g6gVwYMflDX4WqGXhIz1JKrW6WKhMsKAQbvOubHbatWP3e9HeMAGaxQsJ0c7j8pRG48R81vt8XT7jdvaX9jbNE08J60'
# CLIENT_ID = '86b40eb4-ecf5-4c5d-9c20-bd47e85684b8'
# CLIENT_SECRET = 'AU9zaVLOLhua7C3UpJcdmCkWvVZSDn9fh9JGxpXoP6mZYxMRwlBhLQ1sb0VILk7DWsTxM4jKXKZaxWogb0J_NA'



@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer 
    serializer = CreateUserSerializer(data=request.data) 
    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save() 
        # Then we get a token for the created user.
        # This could be done differentley 
        r = requests.post('http://127.0.0.1:8000/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(r.json())
    return Response(serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())



@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
    'http://127.0.0.1:8000/o/token/', 
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/', 
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise) 
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)