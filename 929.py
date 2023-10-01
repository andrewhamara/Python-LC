class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        thing = set()

        for email in emails:

            thing.add(self.splitEmail(email))

        return len(thing)

    def splitEmail(self, email: str) -> List[str]:
        splitter = email.find('@')

        local = email[:splitter]
        local = ''.join([c for c in local if c != '.'])

        domain = email[splitter+1:]

        for i, c in enumerate(local):
            if c == '+':
                return "local: " + local[:i] + "domain: " + domain
        return "local: " + local + "domain: " + domain
