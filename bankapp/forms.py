from django import forms

DISTRICT_CHOICES = [
    ('Alappuzha', 'Alappuzha'),
    ('Kollam', 'Kollam'),
    ('Ernakulam', 'Ernakulam'),
    ('Wayanad', 'Wayanad'),
    ('Thrissur', 'Thrissur')
    # Add more district choices as needed
]

BRANCH_CHOICES = {
    'Alappuzha': ['Changanassery', 'Vandanam', 'Kalarcode'],
    'Kollam': ['Pathanapuram', 'Karunagapally', 'Thodiyoor'],
    'Ernakulam': ['Mattanchery', 'Thoppumbady', 'Kumbalangi'],
    'Wayanad': ['Kalpetta', 'Padinjarathara', 'Meenangadi'],
    'Thrissur': ['Cheruthurithy', 'Vadakkekad', 'Punnayurkkulam']
    # Define sub-areas for other districts
}

ACCOUNT_CHOICES = [
    ('Savings Account', 'Savings Account'),
    ('Current Account', 'Current Account'),
    ('Other', 'Other')
    # Add more account type choices as needed
]

MATERIALS_PROVIDED_CHOICES = [
    ('Debit Card', 'Debit Card'),
    ('Credit Card', 'Credit Card'),
    ('Cheque Book', 'Cheque Book'),
    # Add more materials provided choices as needed
]

class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    dob = forms.DateField(label='Date of Birth',widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.RadioSelect, label='Gender')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    email = forms.EmailField(label='Email')
    address = forms.CharField(widget=forms.Textarea,label='Address')
    district = forms.ChoiceField(choices=DISTRICT_CHOICES, label='District',widget=forms.Select(attrs={'id': 'id_district'}))
    branch = forms.CharField(max_length=200, label='Branch', required=False, widget=forms.Select(attrs={'id': 'id_branch'}))
    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES, label='Account Type')
    materials_provided = forms.MultipleChoiceField(
        choices=MATERIALS_PROVIDED_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Materials Provided'
    )
