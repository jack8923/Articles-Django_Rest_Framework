from ..models import Article, ArticleType
from utility.errors import CustomValidationError


class ArticleHelper:

    @classmethod
    def cneck_title_unique(cls, data):
        articles = Article.objects.all()

        for article in articles:
            if data.get('title') == article.title:
                raise CustomValidationError(
                    {
                        "cause": "Given Titles NOT UNIQUE TOGETHER with"
                    }
                )

    @classmethod
    def cneck_title_and_article_type_unique_together(cls, article_new_title, article_instance):
        articles = Article.objects.all()

        for article in articles:
            if article_instance.title == article.title:
                return False
        return True

    @classmethod
    def check_if_id_is_correct(cls, id):

        articles = Article.objects.all()
        for article in articles:
            if article.id == id:
                return article
        return None

    @classmethod
    def create_or_update(cls, instance, initial_value):

        obj_id = initial_value.get('id')

        if obj_id is not None:
            article_instance = ArticleHelper.check_if_id_is_correct(obj_id)
            if article_instance is not None:
                # print(initial_value.get('title'))
                if article_instance.title == initial_value.get('title') or cls.cneck_title_and_article_type_unique_together(article_instance.title, instance):
                    article_instance.title = instance.title
                    article_instance.author = instance.author
                    article_instance.article_type = instance.article_type
                    article_instance.save()
                else:
                    raise CustomValidationError(
                        {
                            "cause": "Given Title"
                        }
                    )
            else:
                raise CustomValidationError(
                    {
                        "cause": "Given Title NOT UNIQUE"
                    }
                )
        else:
            if cls.cneck_title_and_article_type_unique_together(initial_value.get('title'), instance):
                Article.objects.create(title=initial_value.get('title'), author=initial_value.get('author'),
                                       article_type=initial_value.get('article_type'))
            else:
                raise CustomValidationError(
                    {
                        "cause": "Given Title NOT UNIQUE TOGETHER"
                    }
                )
