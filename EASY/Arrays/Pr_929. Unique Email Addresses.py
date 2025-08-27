class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            # drop everything after the first '+'
            if '+' in local:
                local = local[:local.index('+')]
            # remove dots from local part
            local = local.replace('.', '')
            normalized = local + '@' + domain
            seen.add(normalized)
        return len(seen)
