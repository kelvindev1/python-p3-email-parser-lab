# your code goes here!
import re

class EmailAddressParser:
    email_address = r"[A-z]([A-z0-9][\.]{0,1})+[A-z0-9]+@[A-z0-9]+\.[a-z]{2,}"
    email_regex = re.compile(email_address)

    def __init__ (self, emails):
        self.emails = emails

    def parse(self):
        emails = re.split(r',|\s', self.emails)

        parsed_emails = set()

        for email in emails:
            if self.email_regex.match(email):
                parsed_emails.add(email)

        
        return sorted(list(parsed_emails))