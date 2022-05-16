from django.db import models

class TagTb(models.Model):
  tag_id = models.AutoField(primary_key=True)
  tag_name = models.CharField(max_length=30)
  hit_cnt = models.IntegerField(null=True)
  
  class Meta:
    db_table = 'tag_tb'
    managed = False

class ShopTb(models.Model):
  shop_id = models.AutoField(primary_key=True)
  shop_name = models.CharField(max_length=200)
  shop_desc = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  tel_num = models.CharField(max_length=11)
  parking_info = models.CharField(max_length=255)
  latitude = models.CharField(max_length=20)
  longitude = models.CharField(max_length=20)
  reg_date = models.CharField(max_length=20)
  
  class Meta:
    db_table = 'shop_tb'
    managed = False

class UserTb(models.Model):
  user_id = models.AutoField(primary_key=True)
  user_name = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  password = models.CharField(max_length=255, db_column='pass')
  phone_num = models.CharField(max_length=15, null=True)
  reg_date = models.CharField(max_length=20)
  
  class Meta:
    db_table = 'user_tb'
    managed = False

class FavoriteTb(models.Model):
  shop = models.ForeignKey(ShopTb, on_delete=models.CASCADE, db_column='shop_id')
  user = models.ForeignKey(UserTb, on_delete=models.CASCADE, db_column='user_id')
  reg_date = models.CharField(max_length=20)
  
  class Meta:
    db_table = 'favorite_tb'
    managed = False
  
class ShopTagTb(models.Model):
  seq = models.AutoField(primary_key=True)
  shop = models.ForeignKey(ShopTb, on_delete=models.CASCADE, db_column='shop_id')
  tag = models.ForeignKey(TagTb, on_delete=models.CASCADE, db_column='tag_id')
  
  class Meta:
    db_table = 'shop_tag_tb'
    managed = False