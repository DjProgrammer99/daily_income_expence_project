from django.shortcuts import render,redirect

from .models import Income,IncomeForm
def add_income(request):
    if request.method=='POST':
        f = IncomeForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f = IncomeForm()
        context = {'form':f}
        return render(request,'addIncome.html',context)
    
def income_list(request):
    uid = request.session.get("uid")
    inco = Income.objects.filter(user=uid)
    inco = Income.objects.all()
    return render(request,'incomelist.html',{'inco':inco})