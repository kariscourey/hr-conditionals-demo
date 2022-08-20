customer = {
    "age": 17,
    "parental_consent_form": "signed", # anything else doesn't count
    "safety_class_date": "2001-01-01", # anything other than None counts
}


def customer_can_skydive(customer):
    if ( # .age = no attribute 'age'
        customer.parental_consent_form == "signed" and
        customer.safety_class_date != None # ?? these don't work because dictionary values can't be accessed with dot operator

        # customer.get("parental_consent_form") == "signed" and
        # customer.get("safety_class_date") != None

    ) or customer["age"] >= 18:

    # if customer["age"] >= 18 or ( # .age = no attribute 'age'
    #     # customer.parental_consent_form == "signed" and
    #     # customer.safety_class_date != None # ?? these don't work because dictionary values can't be accessed with dot operator

    #     customer.get("parental_consent_form") == "signed" and
    #     customer.get("safety_class_date") != None

    # ):
        print("can skydive")
        return True
    else:
        print("cannot skydive")
        return False


customer_can_skydive(customer)
