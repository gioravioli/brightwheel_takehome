import re


def clean_phone_number(n):
    return re.sub(r"\D", "", n)


def clean_fields(fields):
    delete = [k for k, v in fields.items() if not v]
    for k in delete:
        del fields[k]
    for k, v in fields.items():
        fields[k] = v.strip()
    if 'phone' in fields:
        fields['phone'] = clean_phone_number(fields['phone'])
    return fields
