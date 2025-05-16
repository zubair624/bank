from django.shortcuts import render
from .models import Account
# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        aadhar = request.POST.get('aadhar')
        acc_type = request.POST.get('acc_type')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        # print(name,phone,gender,aadhar,acc_type,address,dob)
        Account.objects.create(name = name,phone = phone, gender = gender, aadhar = aadhar , account_type = acc_type , address = address , dob = dob)
    return render(request,'create.html')

def pin(request):
    msg = ''
    if request.method == "POST":
        acc = request.POST.get('acc')
        pin = request.POST.get('pin')
        cpin = request.POST.get('cpin')
        # print(acc,pin,cpin)
        if int(pin) == int(cpin):
            account = Account.objects.get(account_number = int(acc))
            account.pin = int(pin)
            account.save()
        else:
            msg = "PIN AND CONFIRM PIN IS NOT MATCHING"

    return render(request,'pin.html',{'msg':msg})


def balance(request):
    account = None
    msg = ''
    if request.method == "POST":
        acc = request.POST.get('acc')
        pin = request.POST.get('pin')
        try:
            account = Account.objects.get(account_number  = int(acc))

        except Exception as e:
            msg = e
        if account.pin == int(pin):
            msg = f" this is your balance {account.amount}"
        else:
            msg = "Invlaid PIN"
    return render(request,'balance.html',{'msg':msg})


def deposit(request):
    msg = ""
    if request.method == "POST":
        acc = request.POST.get('acc')
        pin = request.POST.get('pin')
        amt = request.POST.get('amt')
        account = Account.objects.get(account_number = int(acc))
        if account.pin == int(pin):
            if int(amt)<=10000 and int(amt)>= 500 :
                account.amount+=int(amt)
                account.save()
                msg = f"successfully deposited amount {amt}"
            else:
                msg = "please enter the valid amout"
        else:
            msg = "invliad pin"
    return render(request,'deposit.html',{'msg':msg})


def withdrawl(request):
    msg = ""
    if request.method == "POST":
        acc = request.POST.get('acc')
        pin = request.POST.get('pin')
        amt = request.POST.get('amt')
        account = Account.objects.get(account_number = int(acc))
        if account.pin == int(pin):
            if int(amt)>=100 and int(amt)<= 10000 and int(amt)<account.amount:
                account.amount -=int(amt)
                account.save()
                msg = f" the amount taken is  {amt}"
            else:
                msg = "enter the valid amount"

        else:
            msg = "invalid pin"
    return render(request,'withdrawl.html',{'msg':msg})

def acc_transfer(request):

    msg = ""
    if request.method == "POST":
        from_acc = request.POST.get('facc')
        to_acc = request.POST.get('tacc')
        pin = request.POST.get('pin')
        amt = request.POST.get('amt')
        
        from_account = Account.objects.get(account_number= from_acc)
        to_account = Account.objects.get(account_number= to_acc)
        

        if from_account.pin == int(pin):
            if int(amt)>=100 and int(amt)<= from_account.amount:
                from_account.amount -=int(amt)
                from_account.save()
                to_account.amount +=int(amt)
                to_account.save()
                msg = "transaction completed" 

            
        else:
            msg = "invalid pin"
    return render(request,'acc_transfer.html',{'msg':msg})