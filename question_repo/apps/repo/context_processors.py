from libs.repo_data import user_answer_data
from ..repo.models import Answers,Category

def repo_data(request):
    if request.user.is_authenticated:
        user_data = user_answer_data(request.user)
        hot_question = Answers.objects.hot_question()
        hot_user = Answers.objects.hot_user()
        category = Category.objects.all()
    # current_url = request.path
    return locals()