from django.urls import path
from . import views
from . views import *

urlpatterns = [
	path('', views.home, name='home'),
	path("agents/", Agents, name="agents"),
	path("new-agent/", NewAgent.as_view(), name="new-agent"),
	path("team-leaders/", TeamLeaders, name="team-leaders"),
	path("new-team-leader/", NewTeamLeader.as_view(), name="new-team-leader"),
	path("team-leader-profile/", views.team_leader_profile, name="team-leader-profile"),
	path("my-agents/", views.my_agents, name="my-agents"),
	path("projects/", Projects, name="projects"),
	path("new-project/", NewProject.as_view(), name="new-project"),
	path("invoices/", views.Invoices, name="invoices"),
	path("new-invoice/", NewInvoice.as_view(), name="new-invoice"),
	path("agent-profile/", views.agent_profile, name="agent-profile"),
	path("agent-invoices/", views.agent_invoices, name="agent-invoices"),
	path("approve-invoice/<int:pk>/", ApproveInvoice.as_view(), name="approve-invoice"),
	path("invoice-payment-status/<int:pk>/", ChangeInvoiceStatus.as_view(), name="invoice-payment-status"),
	path("admin-invoices/", views.ApprovedInvoices, name="admin-invoices"),
]