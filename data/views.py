from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from . forms import *
from django.urls import reverse_lazy
import csv
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def export_invoices_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="approved-invoices.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Invoices')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Agent', 'ISP Name', 'Monthly Subscription', 'Date Due', 'Status', 'Date Submitted',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Invoice.objects.filter(approved=True).values_list('agent', 'isp_name', 'monthly_subscription', 'due_date', 'status', 'date_submitted')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

    users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for user in users:
        writer.writerow(user)

    return response

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

	def form_valid(self, form):
		form.instance.project = self.request.user.agent.project
		return super().form_valid(form)

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
	agents = Agent.objects.all()
	context = {
		"hello": "Hello World",
		"agents": agents
	}
	return render(request, "app/my-agents.html", context)

def tl_invoices(request):
	project = TeamLeader.objects.filter(project=request.user.teamleader.project)
	tl_invoices = Invoice.objects.all()
	context = {
		"tl_invoices": tl_invoices,
		"project": project
	}
	return render(request, "app/tl-invoices.html", context)

class ChangeInvoiceStatus(UpdateView):
	model = Invoice
	fields = ["status"]
	template_name = "app/change-invoice-status.html"
	success_url = reverse_lazy("invoices")

class UpdateProject(UpdateView):
	model = Project
	fields = "__all__"
	template_name = "app/update-project.html"


def ApprovedInvoices(request):
	invoices = Invoice.objects.filter(approved=True)
	context = {
		"invoices": invoices
	}
	return render(request, "app/admin-invoices.html", context)


class JobList(ListView):
	model = Job
	template_name = "app/jobs.html"


def tl_projects(request):
	tl_projects = TeamLeader.objects.filter(te=request.user.teamleader)
	context = {
		"tl_projects": tl_projects
	}
	return render(request, "app/tl-projects.html", context)

class UpdateTL(UpdateView):
	model = TeamLeader
	form_class = UpdateTLForm
	template_name = "app/update-tl-profile.html"

class UpdateAgent(UpdateView):
	model = Agent
	form_class = UpdateAgentForm
	template_name = "app/update-agent-profile.html"