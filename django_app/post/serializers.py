from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.Serializer):
    poster_title = serializers.CharField(max_length=30)
    poster_img = serializers.ImageField()
    genre = serializers.CharField(max_length=30)
    grade = serializers.IntegerField()
    fee = serializers.IntegerField()
    location = serializers.CharField(max_length=30)
    place = serializers.CharField(max_length=30)
    thumbnail_img_1 = serializers.ImageField()
    thumbnail_img_2 = serializers.ImageField()
    time = serializers.TimeField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()


    def create(self, validated_data):
        poster_title = self.validated_data.get('poster_title', '')
        poster_img = self.validated_data.get('poster_img', '')
        genre = self.validated_data.get('genre', '')
        grade = self.validated_data.get('grade', '')
        fee = self.validated_data.get('fee', '')
        location = self.validated_data.get('location', '')
        place = self.validated_data.get('place', '')
        thumbnail_img_1 = self.validated_data.get('thumbnail_img_1', '')
        thumbnail_img_2 = self.validated_data.get('thumbnail_img_2', '')
        time = self.validated_data.get('time', '')
        date_start = self.validated_data.get('date_start', '')
        date_end = self.validated_data.get('date_end', '')


        poster = Post.objects.create(
            poster_title=poster_title,
            poster_img=poster_img,
            genre=genre,
            grade=grade,
            fee=fee,
            location=location,
            place=place,
            thumbnail_img_1=thumbnail_img_1,
            thumbnail_img_2=thumbnail_img_2,
            time=time,
            date_start=date_start,
            date_end=date_end,
        )
        return poster



