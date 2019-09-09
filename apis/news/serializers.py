from rest_framework.serializers import ModelSerializer
from apis.news.models import News

class NewsSerializer(ModelSerializer):

    class Meta:
        model = News
        # fields =  "pk", "title", "story", "category", "created_at", "updated_at"
        fields = "__all__"
        # exclude = 
        # extra_kwargs = {
        #     "reporter": {"required": False}
        # }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        context = kwargs.get('context')
        if context:
            self.request = context.get('request')

    def create(self, validate_data):
        news = News(**validate_data)
        news.reporter = self.request.user
        news.save()
        return news
