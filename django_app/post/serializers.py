from django.contrib.auth.models import User
from django.forms import widgets
from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')

    class Meta:
        model = Post
        fields = ('url', 'highlight', 'owner',
                  'code', 'linenos',
                  'language', 'style', 'poster_title',
                  'poster_img', 'genre', 'grade', 'fee',
                  'location', 'place', 'thumbnail_img_1',
                  'thumbnail_img_2', 'time', 'date_start', 'date_end')

    def create(self, validated_data):
        """
        검증한 데이터로 새 `Snippet` 인스턴스를 생성하여 리턴합니다.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        검증한 데이터로 기존 `Snippet` 인스턴스를 업데이트한 후 리턴합니다.
        """
        # instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.style = validated_data.get('poster_title', instance.style)
        instance.style = validated_data.get('poster_img', instance.style)
        instance.style = validated_data.get('genre', instance.style)
        instance.style = validated_data.get('grade', instance.style)
        instance.style = validated_data.get('fee', instance.style)
        instance.style = validated_data.get('location', instance.style)
        instance.style = validated_data.get('place', instance.style)
        instance.style = validated_data.get('thumbnail_img_1', instance.style)
        instance.style = validated_data.get('thumbnail_img_2', instance.style)
        instance.style = validated_data.get('time', instance.style)
        instance.style = validated_data.get('date_start', instance.style)
        instance.style = validated_data.get('date_end', instance.style)

        instance.save()
        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'posts')
