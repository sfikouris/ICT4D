from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('rec_name', 'rec_location', 'rec_commune', 'cercle_num', 
                    'tree_num', 'tree_count', 'chosen_language','phone',)