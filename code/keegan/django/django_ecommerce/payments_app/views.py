from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Receipt, ReceiptItem
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


    line_items=[]

    for cart_item in request.user.cart.cart_items.all():
        line_items.append({
            'quantity': cart_item.quantity,
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(cart_item.product.price * 100), # convert price to pennies
                'product_data': {
                    'name': cart_item.product.title,
                    'images': [cart_item.product.image_url]
                }
            }
        })


    try:
        # create stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            mode='payment',
            payment_method_types=['card'],
            success_url=f"http://localhost:8000/payments/receipt/{request.user.username}",
            cancel_url=f"http://localhost:8000/users/{request.user.username}",
           
            # line_items contains all the product data
            line_items = line_items
            # line_items = [
            #     {
            #         'quantity': 1,
            #         'price_data': {
            #             'currency': 'usd',
            #             'unit_amount': 1000,
            #             'product_data': {
            #                 'name': 'test product',
            #                 'images': ['https://picsum.photos/200/300']
            #             }
            #         }
            #     }
            # ]
        )
        return JsonResponse({'sessionId': checkout_session.id})
    except Exception as error:
        print(error)
        return redirect('users_app:detail', request.user.username)


def receipt(request, username):
    # get the requested user from the database
    user = get_object_or_404(get_user_model(), username=username)

    # create a new receipt for the requested user
    new_receipt = Receipt.objects.create(user=user)

    # loop through the CartItems in the user's cart
    for cart_item in user.cart.cart_items.all():
        # create a ReceiptItem with all the data from the current CartItem
        ReceiptItem.objects.create(
            product=cart_item.product,
            receipt=new_receipt,
            quantity=cart_item.quantity
        )

        # delete the CartItem
        cart_item.delete()

    return redirect('shop_app:index')