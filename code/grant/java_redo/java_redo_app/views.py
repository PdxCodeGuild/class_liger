from django.shortcuts import render

# Create your views here.



def base(request):

   

    return render(request, 'base.html')

def uc(request):

    return render(request, 'unit_converter.html')

def cc(request):

    return render(request, 'cc_valid.html')

def pw(request):

    return render(request, 'pw_gen.html')