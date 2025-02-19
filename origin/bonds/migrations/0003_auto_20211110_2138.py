# Generated by Django 2.2.24 on 2021-11-10 21:38

import bonds.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonds', '0002_bond_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bond',
            name='currency',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='Invalid currency', regex='^(AED|AFN|ALL|AMD|ANG|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BOV|BRL|BSD|BTN|BWP|BYN|BZD|CAD|CDF|CHE|CHF|CHW|CLF|CLP|CNY|COP|COU|CRC|CUC|CUP|CVE|CZK|DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|FJD|FKP|GBP|GEL|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|INR|IQD|IRR|ISK|JMD|JOD|JPY|KES|KGS|KHR|KMF|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|MNT|MOP|MRU|MUR|MVR|MWK|MXN|MXV|MYR|MZN|NAD|NGN|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SRD|SSP|STN|SVC|SYP|SZL|THB|TJS|TMT|TND|TOP|TRY|TTD|TWD|TZS|UAH|UGX|USD|USN|UYI|UYU|UYW|UZS|VED|VES|VND|VUV|WST|XAF|XAG|XAU|XBA|XBB|XBC|XBD|XCD|XDR|XOF|XPD|XPF|XPT|XSU|XTS|XUA|XXX|YER|ZAR|ZMW|ZWL)$')]),
        ),
        migrations.AlterField(
            model_name='bond',
            name='isin',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Invalid isin', regex='^[0-9a-zA-Z]$')]),
        ),
        migrations.AlterField(
            model_name='bond',
            name='lei',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Invalid lei', regex='^[0-9a-zA-Z]$')]),
        ),
        migrations.AlterField(
            model_name='bond',
            name='maturity',
            field=models.DateField(validators=[bonds.models.validate_maturity]),
        ),
    ]
