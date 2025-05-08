from bisect import bisect_left
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            start = bisect_left(products, prefix)

            # Collect up to 3 products starting with the current prefix
            suggestions = []
            for i in range(start, min(start + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
            
            result.append(suggestions)
        
        return result

        
