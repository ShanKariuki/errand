from django import forms

from . models import*
INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'
class TodoForm(forms.ModelForm):

    class Meta:
      model=Task
      fields=('name','title','description','due_date','address',)
      widgets={
             'name':forms.Select(attrs={
              'class':INPUT_CLASSES,
           
       }),
       'title':forms.TextInput(attrs={
              'class':INPUT_CLASSES,
              'placeholder':'Enter the task name'
       }),
       'description':forms.Textarea(attrs={
              'class':INPUT_CLASSES,
              'placeholder':'Description about the task'
       }),
      
       'due_date':forms.DateInput(attrs={
          'type': 'date', 
          'placeholder': 'yyyy-mm-dd (DOB)',
          'class':INPUT_CLASSES,
          
       }),
       'address':forms.TextInput(attrs={
              'class':INPUT_CLASSES,
              'placeholder':'Enter the Location or address number'
       }),
        }
      