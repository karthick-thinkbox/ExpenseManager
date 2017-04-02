from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from .forms import addexpense,addcat
from .models import expense,category
from django.contrib.auth import logout
from django.db.models import Sum
from .tables import cat_table
from django_tables2 import RequestConfig
@login_required
def dash(request):
    current_user=request.user
    qryset=expense.objects.values('category').annotate(tot=Sum('amount'))
    master=[]
    master.append(['Task', 'link', 'Hours per Day'])
    for i in qryset:
        cat=i.get('category')
        sum=i.get('tot')
        link='/cat/'+cat+'/'
        lis=[]
        lis.append(cat)
        lis.append(link)
        lis.append(sum)
        master.append(lis)
    return render(request,'base.html',{'dict':master})
    
        
@login_required
def entry(request):
    if request.method == "POST":
        addform=addexpense(request.POST)
        if addform.is_valid():
            cat=addform.cleaned_data['cat']
            amnt=addform.cleaned_data['Amount']
            desc=addform.cleaned_data['Decription']
            current_user=request.user
            try:
                row=expense(category=cat,amount=amnt,Description=desc,user=current_user)
                row.save()
                form1=addexpense()
                form2=addcat()
                return render(request,'expense.html',{'form1':form1,'form2':form2,'stat':'exadd'})
            except Exception as e:
                form1=addexpense()
                form2=addcat()
                return render(request,'expense.html',{'form1':form1 ,'form2':form2,'stat':'False','msg':str(e)})
        
        else:   
             form1=addexpense()
             form2=addcat()
             return render(request,'expense.html',{'form1':form1,'form2':form2,'stat':'Invalid'})    
                
        
         
    else:
        form1=addexpense()
        form2=addcat()
        return render(request,'expense.html',{'form1':form1,'form2':form2})
@login_required
def cat(request):
    if request.method == "POST":
        catform=addcat(request.POST)
        if catform.is_valid():
            
            cat=catform.cleaned_data['value']
            try:
                row=category(value=cat)
                row.save()
                form1=addexpense()
                form2=addcat()
                return render(request,'expense.html',{'form1':form1,'form2':form2,'stat':'catadd'})
            except Exception as e:
                form1=addexpense()
                form2=addcat()
                return render(request,'expense.html',{'form1':form1 ,'form2':form2,'stat':'False','msg':str(e)})
        else:
            form1=addexpense()
            form2=addcat()
            return render(request,'expense.html',{'form1':form1,'form2':form2,'stat':'False','msg':'Category Already exists'})
    else:
        form1=addexpense()
        form2=addcat()
        return render(request,'expense.html',{'form1':form1 ,'form2':form2})
    
@login_required
def exitpage(request):
    logout(request)
    return render (request,'logout.html')
        
    
    
    
    

@login_required
def table(request,pk):
    qset=expense.objects.filter(user=request.user ,category=pk)
    table=cat_table(qset)
    RequestConfig(request).configure(table)
    return render(request,'detail.html',{'table':table})
    