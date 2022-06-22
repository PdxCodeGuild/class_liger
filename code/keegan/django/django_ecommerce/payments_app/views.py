from django.shortcuts import render, redirect
from django.http import JsonResponse
import decouple
import stripe

# set the secret key within stripe using the value from the .env file
stripe.api_key = decouple.config('STRIPE_SECRET_KEY')

def stripe_config(request):
    '''return the stripe public key as JSON'''

    # retrieve the API public key from the .env file
    public_key = decouple.config('STRIPE_PUBLISHABLE_KEY')
    stripe_config = {'publicKey': public_key}

    return JsonResponse(stripe_config)


def checkout(request):
    '''create a new Stripe session and return the session id as JSON'''

    try:
        # create stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            mode='payment',
            payment_method_types=['card'],
            success_url=f"http://localhost:8000/users/{request.user.username}",
            cancel_url=f"http://localhost:8000/users/{request.user.username}",
           
            # line_items contains all the product data
            line_items = [
                {
                    'quantity': 1,
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 1000,
                        'product_data': {
                            'name': 'test product',
                            'images': ['https://picsum.photos/200/300']
                        }
                    }
                }
            ]
        )
        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as error:
        print(error)
        return redirect('users_app:detail', request.user.username)
