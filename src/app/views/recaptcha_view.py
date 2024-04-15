from rest_framework.response import Response
from rest_framework.decorators import api_view
from decouple import config
import requests


@api_view(['POST'])
def RecaptchaView(request):
    captcha_token = request.data.get('captcha_token')

    if not captcha_token:
        return Response({'error': 'No token provided'}, status=400)

    response = requests.post('https://www.google.com/recaptcha/api/siteverify',
                             data={
                                 'secret': config('RECAPTCHA_SECRET_KEY'),
                                 'response': captcha_token
                             })

    result = response.json()

    if result.get('success'):
        return Response({'success': 'El token es valido'}, status=200)
    else:
        return Response({'fail': result.get('error-codes')[0]}, status=400)
