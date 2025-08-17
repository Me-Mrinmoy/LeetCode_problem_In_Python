class Solution(object):
    def subdomainVisits(self, cpdomains):
        counts = {}

        for entry in cpdomains:
            cnt_str, domain = entry.split()
            cnt = int(cnt_str)
            parts = domain.split('.')

            # add counts for each subdomain suffix
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                counts[sub] = counts.get(sub, 0) + cnt

        # build result in any order
        return ["{} {}".format(v, k) for k, v in counts.items()]
