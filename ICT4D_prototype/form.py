from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('rec_commune','rec_location','rec_name','tree_num','phone','chosen_language','tree_count','cercle_num',)
        #'cercle_num','tree_count','chosen_language','phone',