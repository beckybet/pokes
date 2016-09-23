from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
	if "user_id" in request.session:
		return redirect('success')

	return render(request, "ex/main.html")


def success(request):
	if request.session not in session:
		return redirect('index')
		
	context={
		"users": User.objects.all(), 
		"this_user": User.objects.get(id=request.session['user_id'])
	}
	return render(request, "users/success.html", context)
	
def register(request):
	if request.method == "POST":
		response = User.objects.register(request.POST)

		if response["registered"]:
			request.session["user_id"] = response["user"].id
			return redirect("success")
		else:
			for error in response["errors"]:
				messages.error(request, error)
	
	return redirect("index")
def login(request):
	if request.method == "POST":
		user = User.object.login(request.POST)
		if user: 
			request.session['user_id'] = user.id
			return redirect('success')
		else:
			messages.error(request, "Email or password incorrect.")
	return redirect('index')


def logout(request):
	request.session.clear()
	return redirect('index')
