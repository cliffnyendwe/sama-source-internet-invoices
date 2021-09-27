from django import forms
from . models import Agent, TeamLeader, Invoice

class AddAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('user', 'name', 'ssdc_number', 'project', 'team_leader', 'payment_method', 'installation')

        widgets = {
        	'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ssdc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'team_leader': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}), 
            'installation': forms.NumberInput(attrs={'class': 'form-control'}), 
        }

class UpdateAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ('user', 'name', 'ssdc_number', 'project', 'team_leader', 'payment_method', 'installation')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ssdc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
            'team_leader': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}), 
            'installation': forms.NumberInput(attrs={'class': 'form-control'}),        
        }

class AddTeamLeaderForm(forms.ModelForm):
    class Meta:
        model = TeamLeader
        fields = ('user', 'name', 'ssdc_number', 'project')

        widgets = {
        	'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ssdc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),

        }

class UpdateTLForm(forms.ModelForm):
    class Meta:
        model = TeamLeader
        fields = ('user', 'name', 'ssdc_number', 'project')

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ssdc_number': forms.TextInput(attrs={'class': 'form-control'}),
            'project': forms.Select(attrs={'class': 'form-control'}),      
        }

class AddInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('agent', 'isp_name', 'monthly_subscription', 'invoice_file')

        widgets = {
            'agent': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'agent', 'type': 'hidden'}),
            'isp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'monthly_subscription': forms.NumberInput(attrs={'class': 'form-control'}),
            'invoice_file': forms.FileInput(attrs={'class': 'form-control'}),
        }
