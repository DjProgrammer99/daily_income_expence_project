from django.shortcuts import render,redirect
from .models import Expence,ExpenceForm
def add_expence(request):
    if request.method=='POST':
        f = ExpenceForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f = ExpenceForm()
        context = {'form':f}
        return render(request,'addExpence.html',context)
    
def expence_list(request):
    expo = Expence.objects.all()
    return render(request,'expencelist.html',{'expo':expo})

def update_user(request,id):
    user=Expence.objects.get(id=id)
    if request.method=='POST':
        f=ExpenceForm(request.POST,instance=user)
        f.save()
        return redirect('/addexpence')
    else:
        f=ExpenceForm(instance=user)
        context={"form":f}
        return render(request,"addexpence.html",context)
    
def delete_user(request,id):
    d = Expence.objects.get(id=id) 
    d.delete()
    return redirect('/') 


    
