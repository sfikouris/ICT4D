from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('rec_commune','rec_location','tree_num',)
        #'cercle_num','tree_count','chosen_language','phone',