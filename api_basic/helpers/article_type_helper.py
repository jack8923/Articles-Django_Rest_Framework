from ..models import ArticleType
from utility.errors import CustomValidationError

class ArticleTypeHelper:

    @classmethod
    def check_unique(cls,new_name):

        names = ArticleType.objects.all()
        for name in names:
            if new_name == str(name):
                raise CustomValidationError(
                    {
                        "cause": "Given article_type NOT UNIQUE TOGETHER with"
                    }
                )