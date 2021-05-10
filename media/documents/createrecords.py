from django.core.management import setup_environ
import settings
setup_environ(settings)

from mixer.backend.django import mixer
from ICT4D_prototype.models import Document

clients = mixer.cycle(4).blend(Document, tree_count=(count for count in (1,2,3,4)))

#this is just some note for me to add documents in the database
