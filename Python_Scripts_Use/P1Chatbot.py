# Define a dictionary of frequently asked questions for each category
FAQs = {
    "billing": {
        "How do I update my billing information?": "You can update your billing information by logging into your account and clicking on the 'Billing' tab.",
        "When will my payment be processed?": "Payments are processed on the date that they are due."
    },
    "product information": {
        "What is your return policy?": "Our return policy allows for returns within 30 days of purchase.",
        "What materials is the product made of?": "The product is made of high-quality stainless steel."
    },
    "technical support": {
        "How do I troubleshoot a problem with the product?": "You can troubleshoot the product by checking the user manual or contacting our technical support team at 555-555-5555.",
        "What are your support hours?": "Our support hours are 9am-5pm EST, Monday-Friday."
    }
}

# Define a dictionary of relevant phone numbers for each category
PHONE_NUMBERS = {
    "billing": "555-555-5555",
    "product information": "555-555-5556",
    "technical support": "555-555-5557"
}

def send_alarm(message):
    # Send an alarm to employees (e.g. through email or SMS)
    pass

def handle_customer_query(query):
    # Determine the category of the customer's issue
    category = None
    for c in FAQs.keys():
        if query in FAQs[c]:
            category = c
            break
    if category is None:
        # If the query is not covered by the FAQs, provide the relevant phone number
        return "I'm sorry, I don't have an answer for that. Please contact us at " + PHONE_NUMBERS[category] + " for further assistance."
    else:
        # If the query is covered by the FAQs, provide the answer
        answer = FAQs[category][query]
        if "urgent" in query or "emergency" in query:
            send_alarm("Urgent issue: " + query)
        return answer
