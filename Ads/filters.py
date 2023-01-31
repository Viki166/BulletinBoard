from django_filters import FilterSet
from Ads.models import Comment


class CommentsFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'ad': ['exact'],
        }
        
