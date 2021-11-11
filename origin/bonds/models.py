from logging import currentframe
from django.contrib.auth.models import User  
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models
from datetime import date

# REGEX
currency = "^(AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BOV|BRL|BSD|BTN|BWP|BYN|BZD|CAD|CDF|CHE|CHF|CHW|CLF|CLP|CNY|COP|COU|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|INR|IQD|IRR|ISK|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRU|MUR|MVR|MWK|MXN|MXV|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SRD|SSP|STN|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TWD|TZS|UAH|UGX|USD|USN|UYI|UYU|UYW|UZS|VED|VES|VND|VUV|WST|XAF|XAG|XAU|XBA|XBB|XBC|XBD|XCD|XDR|XOF|XPD|XPF|XPT|XSU|XTS|XUA|XXX|YER|ZAR|ZMW|ZWL)$"
def validate_maturity(maturity):
    today = date.today()
    if today >= maturity:
        raise ValidationError('Invalid maturity')

class Bond(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    isin = models.CharField(max_length=12, validators=[RegexValidator(regex="^[0-9a-zA-Z]+$", message="Invalid isin")])
    size = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, validators=[RegexValidator(regex=currency, message="Invalid currency")])
    maturity = models.DateField(validators=[validate_maturity])
    lei = models.CharField(max_length=20, validators=[RegexValidator(regex="^[0-9a-zA-Z]+$", message="Invalid lei")])
    legal_name = models.CharField(max_length=100)

    def __str__(self):
        return self.isin