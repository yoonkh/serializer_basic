from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
GRADE_CHOICES = (
        (0, '전체관람가'),
        (12, '12세이상 관람가'),
        (15, '15세이상 관람가'),
        (18, '청소년 관람불가'),
    )

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='posts')
    highlighted = models.TextField()

    poster_title = models.CharField(max_length=30)
    poster_img = models.ImageField(upload_to='poster/post_img/')
    genre = models.CharField(max_length=30)
    grade = models.IntegerField(choices=GRADE_CHOICES, help_text='관람 선택', default=1)
    fee = models.IntegerField()
    location = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    thumbnail_img_1 = models.ImageField(upload_to='poster/thumbnail_1/')
    thumbnail_img_2 = models.ImageField(upload_to='poster/thumbnail_2/')
    time = models.TimeField(help_text='HH:MM')
    date_start = models.DateField(help_text='YYYY-MM-DD')
    date_end = models.DateField(help_text='YYYY-MM-DD')

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        # lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, formatter)
        super(Post, self).save(*args, **kwargs)

