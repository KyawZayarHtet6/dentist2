from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def index(request):
	return render(request,'index.html',{})

def contact(request):


	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email =request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(

			message_name,#subject
			message,#message
			message_email,#from email
			['kyhtet2468@gmail.com'],#to email
			)
		return render(request,'contact.html',{'message_name':message_name})

	else:
		return render(request,'contact.html',{})

def appointment(request):

	if request.method == 'POST':

		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']


		appointment = 'My name: ' + " is " + str(your_name) + '\n' + 'My Phone: ' + str(your_phone)+ '\n' + 'My Address: ' + str(your_address)+ '\n' + 'My Schedule: '+ str(your_schedule)+ '\n' + 'My time: ' + str(your_time)+ '\n' +"My Message: " + str(your_message) 

		# send an email
		send_mail(

			"Appointment Message From: " + " " + str(your_name),#subject
			appointment,#message
			your_email,#from email
			['kyhtet2468@gmail.com'],#to email
			)

		return render(request,'appointment.html',{

			'your_name':your_name,
			'your_phone':your_phone,
			'your_email':your_email,
			'your_address':your_address,
			'your_schedule':your_schedule,
			'your_time':your_time,
			'your_schedule':your_schedule})





			

	else:
		return render(request,'index.html',{})



def about(request):
	return render(request,'about.html',{})

def blog_detail(request):
	return render(request,'blog-details.html',{})

def blog(request):
	return render(request,'blog.html',{})

def pricing(request):
	return render(request,'pricing.html',{})

def service(request):
	return render(request,'service.html',{})