from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from . forms import *
from django.urls import reverse_lazy
# Create your views here.
@login_required(login_url="/login/")
def home(request):
	return render(request, "index.html")

@login_required(login_url="/login/")
def TeamLeaders(request):
	team_leaders = TeamLeader.objects.all()
	template_name = "app/team-leaders.html"
	return render(request, template_name, {"team_leaders": team_leaders})

class NewTeamLeader(CreateView):
	model = TeamLeader
	form_class = AddTeamLeaderForm
	template_name = "app/new-team-leader.html"

@login_required(login_url="/login/")
def Agents(request):
	agents = Agent.objects.all()
	template_name = "app/agents.html"
	return render(request, template_name, {"agents": agents})

class NewAgent(CreateView):
	model = Agent
	form_class = AddAgentForm
	template_name = "app/new-agent.html"

@login_required(login_url="/login/")
def Projects(request):
	projects = Project.objects.all() 
	template_name = "app/projects.html"
	return render(request, template_name, {"projects": projects})

class NewProject(CreateView):
	model = Project
	fields = "__all__"
	template_name = "app/new-project.html"

@login_required(login_url="/login/")
def Invoices(request):
	invoices = Invoice.objects.all()
	template_name = "app/invoices.html"
	return render(request, template_name, {"invoices": invoices})

class NewInvoice(CreateView):
	model = Invoice
	form_class = AddInvoiceForm
	template_name = "app/new-invoice.html"

def agent_profile(request):
	agent = Agent.objects.filter(user=request.user)
	print("Agent is: ",agent)
	context = {
		"agent": agent
	}
	return render(request, "agent-profile.html", context)

def agent_invoices(request):
	agent = Agent.objects.filter(user=request.user)
	agent_invoices = Invoice.objects.filter(agent=request.user.agent)

	context = {
		"agent": agent,
		"agent_invoices": agent_invoices
	}
	return render(request, "app/agent-invoices.html", context)

class ApproveInvoice(UpdateView):
	model = Invoice
	fields = ["approved"]
	template_name = "app/approve-invoice.html"
	success_url = reverse_lazy("invoices")

def team_leader_profile(request):
	return render(request, "team-leader-profile.html")

def my_agents(request):
	project = TeamLeader.objects.filter(project=request.user.teamleader.project)

	context = {
		"hello": "Hello World"
	}
	return render(request, "app/my-agents.html", context)

class ChangeInvoiceStatus(UpdateView):
	model = Invoice
	fields = ["status"]
	template_name = "app/change-invoice-status.html"
	success_url = reverse_lazy("invoices")

def ApprovedInvoices(request):
	invoices = Invoice.objects.filter(approved=True)
	context = {
		"invoices": invoices
	}
	return render(request, "app/admin-invoices.html", context)