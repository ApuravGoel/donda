from django.db import models

class Employee(models.Model):
    case_number = models.CharField("case_number", max_length=20)
    case_status = models.CharField("case_status", max_length=50)
    case_submitted = models.DateField("case_submitted")
    decision_date = models.DateField("decision_date")
    visa_class = models.CharField("visa_class", max_length=10)
    employment_start_date = models.DateField("employment_start_date")
    employment_end_date = models.DateField("employment_end_date")
    employer_name = models.CharField("employer_name", max_length=255)
    employer_address = models.CharField("employer_address", max_length=255)
    employer_city = models.CharField("employer_city", max_length=100)
    employer_state = models.CharField("employer_state", max_length=50)
    employer_postal_code = models.CharField("employer_postal_code", max_length=20)
    employer_country = models.CharField("employer_country", max_length=100)
    employer_province = models.CharField("employer_province", max_length=100, null=True, blank=True)
    employer_phone = models.CharField("employer_phone", max_length=20)
    employer_phone_ext = models.CharField("employer_phone_ext", max_length=10, null=True, blank=True)
    agent_attorney_name = models.CharField("agent_attorney_name", max_length=255)
    agent_attorney_city = models.CharField("agent_attorney_city", max_length=100)
    agent_attorney_state = models.CharField("agent_attorney_state", max_length=50)
    job_title = models.CharField("job_title", max_length=255)
    soc_code = models.CharField("soc_code", max_length=10)
    soc_name = models.CharField("soc_name", max_length=255)
    naic_code = models.CharField("naic_code", max_length=10)
    total_workers = models.IntegerField("total_workers")
    full_time_position = models.CharField("full_time_position")
    prevailing_wage = models.DecimalField("prevailing_wage", max_digits=12, decimal_places=2)
    pw_unit_of_pay = models.CharField("pw_unit_of_pay", max_length=10)
    pw_wage_source = models.CharField("pw_wage_source", max_length=255)
    pw_source_year = models.IntegerField("pw_source_year")
    pw_source_other = models.CharField("pw_source_other", max_length=255, null=True, blank=True)
    wage_rate_of_pay_from = models.DecimalField("wage_rate_of_pay_from", max_digits=12, decimal_places=2)
    wage_rate_of_pay_to = models.DecimalField("wage_rate_of_pay_to", max_digits=12, decimal_places=2)
    wage_unit_of_pay = models.CharField("wage_unit_of_pay", max_length=10)
    h1b_dependent = models.CharField("h1b_dependent", max_length=1)
    willful_violator = models.CharField("willful_violator", max_length=1)
    worksite_city = models.CharField("worksite_city", max_length=100)
    worksite_county = models.CharField("worksite_county", max_length=100)
    worksite_state = models.CharField("worksite_state", max_length=50)
    worksite_postal_code = models.CharField("worksite_postal_code", max_length=20)
    original_cert_date = models.DateField("original_cert_date")
