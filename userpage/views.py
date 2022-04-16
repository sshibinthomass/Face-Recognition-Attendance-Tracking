from django.shortcuts import render
from userpage.models import UserDetails


# Create your views here.
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def createUser(request):
    len_det=len(UserDetails.objects.all())
    lst=[]
    firstName = request.POST["firstName"]  
    lastName = request.POST["lastName"] 
    userName = request.POST["userName"] 
   
    age = int(request.POST["age"])
    dateOfBirth = request.POST["dateOfBirth"] 
    gender=request.POST["gender"]  
    address = request.POST["address"] 
    email = request.POST["email"] 
    password = request.POST["password"] 
    phone=request.POST["phone"] 
    val=UserDetails(empId="EMP"+str(len_det+1),empFirstName=firstName,empLastName=lastName,empUserName=userName,empAge=age,empDOB=dateOfBirth,empGender=gender,empAddress=address,empPhone=phone,password=password,is_active=True)
    val.save()
    return render(request,'result.html',{'result':firstName})

def checkUsers(request):
    UserDetail1s=UserDetails.objects.all()
    for i in UserDetail1s:
        print(i.empFirstName)
    return render(request,'users.html',{'result':UserDetail1s})