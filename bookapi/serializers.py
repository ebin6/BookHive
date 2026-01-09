from rest_framework import serializers
from manager.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=["id","name","place","about",
                "image","dob","slug"]