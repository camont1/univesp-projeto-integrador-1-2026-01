from django import forms

# ProfileForm define o formulário de perfil do usuário, que é usado tanto para criar um novo usuário quanto para editar o perfil existente. 
# Ele herda de forms.Form, o que significa que é um formulário simples, não vinculado a um modelo específico.

class ProfileForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nome", max_length=100)
    last_name = forms.CharField(label="Sobrenome", max_length=100)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    # Os métodos abaixo são usados para validar os campos do formulário. 
    # São chamados automaticamente quando o método is_valid() é chamado no formulário. 
    # Os critérios de validação utilizados aqui são apenas exemplos e podem ser ajustados 
    # conforme necessário para atender aos requisitos específicos do projeto.   
    def clean_username(self):
            username = self.cleaned_data['username']
            if len(username) < 3:
                raise forms.ValidationError("Username must be at least 3 characters long.")
            return username
    def clean_password(self):
            password = self.cleaned_data['password']
            if len(password) < 6:
                raise forms.ValidationError("Password must be at least 6 characters long.")
            return password
    def clean_email(self):            
            email = self.cleaned_data['email']
            if email.endswith('@example.com'):
               raise forms.ValidationError("Email must not be from the domain @example.com.")
            return email
    def clean_first_name(self):
            first_name = self.cleaned_data['first_name']
            if not first_name.isalpha():
                raise forms.ValidationError("First name must contain only letters.")
            return first_name
    def clean_last_name(self):
            last_name = self.cleaned_data['last_name']
            if not last_name.isalpha():
                raise forms.ValidationError("Last name must contain only letters.")
            return last_name