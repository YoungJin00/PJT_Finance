from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융상품코드
    kor_co_nm = models.TextField(default='none') # 금융회사명
    fin_prdt_nm = models.TextField(default='none') # 금융상품명
    etc_note = models.TextField(default='none') # 금융상품설명
    join_deny = models.IntegerField(default=-1) #  가입제한 (1: 제한X, 2:서민전용, 3: 일부제한)
    join_member = models.TextField(default='none') # 가입대상
    join_way = models.TextField(default='none') # 가입방법
    spcl_cnd = models.TextField(default='none') # 우대조건

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='deposit_options')
    fin_prdt_cd = models.TextField(default='none') # 금융상품 코드
    intr_rate_type_nm = models.CharField(max_length=100, default='none') # 저축금리 유형명
    intr_rate = models.FloatField(null= True, default=-1) # 저축금리
    intr_rate2 = models.FloatField(null= True, default=-1) # 최고 우대 금리
    save_trm = models.IntegerField(default=-1) # 저축기간 (단위:개월)
