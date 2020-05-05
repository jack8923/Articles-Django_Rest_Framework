from ..models import Author
from utility.errors import CustomValidationError

class AuthorHelper:

    @classmethod
    def check_unique(cls,data):

        names = ArticleType.objects.all()
        for name in names:
            if name == new_name:
                raise CustomValidationError(

                )