from django.shortcuts import render

# Create your views here.
def ifelse(request):
    d={'a':50,'b':52}
    return render(request,'ifelse.html',d)
    
    