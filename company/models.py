from django.db import models

class Jobs(models.Model):
  job_id = models.CharField(max_length=10, primary_key=True)
  job_title = models.CharField(max_length=35, null=True)
  min_salary = models.IntegerField(null=True)
  max_salary = models.IntegerField(null=True)
  
  class Meta:
    db_table = 'JOBS'
    managed = False

class Regions(models.Model):
  region_id = models.AutoField(primary_key=True)
  region_name = models.CharField(max_length=25, null=True)
  
  class Meta:
    db_table = 'REGIONS'
    managed = False

class Countries(models.Model):
  country_id = models.CharField(max_length=2, primary_key=True)
  country_name = models.CharField(max_length=40, null=True)
  region = models.ForeignKey(Regions, on_delete=models.CASCADE, db_column='region_id', null=True)

  class Meta:
    db_table = 'COUNTRIES'
    managed = False

class Locations(models.Model):
  location_id = models.AutoField(primary_key=True)
  street_address = models.CharField(max_length=40, null=True)
  postal_code = models.CharField(max_length=12, null=True)
  city = models.CharField(max_length=30, null=True)
  state_province = models.CharField(max_length=25, null=True)
  country = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='country_id', null=True)
  
  class Meta:
    db_table = 'LOCATIONS'
    managed = False
  
class Departments(models.Model):
  department_id = models.AutoField(primary_key=True)
  department_name = models.CharField(max_length=30, null=True)
  location = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column='location_id', null=True)
  
  class Meta:
    db_table = 'DEPARTMENTS'
    managed = False
  
class Employees(models.Model):
  employee_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=20, null=True)
  last_name = models.CharField(max_length=25, null=True)
  email = models.CharField(max_length=25, null=True)
  phone_number = models.CharField(max_length=20, null=True)
  hire_date = models.DateField(null=True)
  job = models.ForeignKey(Jobs, on_delete=models.CASCADE, db_column='job_id', null=True)
  salary = models.IntegerField(null=True)
  commission_pct = models.IntegerField(null=True)
  manager = models.ForeignKey('self', on_delete=models.SET_NULL, db_column='manager_id', null=True)
  department = models.ForeignKey(Departments, on_delete=models.CASCADE, db_column='department_id', null=True)
  
  class Meta:
    db_table = 'EMPLOYEES'
    managed = False
  
class JobHistory(models.Model):
  job_history_id = models.AutoField(primary_key=True)
  emplo = models.ForeignKey(Locations, on_delete=models.CASCADE, db_column='location_id', null=True)
  department_name = models.CharField(max_length=30, null=True)
  
  class Meta:
    db_table = 'JOB_HISTORY'
    managed = False
  

  
