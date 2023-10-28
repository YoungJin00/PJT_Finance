from django.contrib.auth.forms import UserCreationForm

# model 선택 세가지 방법
# 1.  직접 가져오기
# from .models import User
# 2. settings 에 설정된 모델 가져오기
# from django.conf import settings # model = settings.AUTH_USER_MODEL
# > 문자열 > models.py 에 작성할 떄는 문자열로 적는게 좋다
# 3. get_user_model 메서들 활용
from django.contrib.auth import get_user_model


class CustomUsercreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields