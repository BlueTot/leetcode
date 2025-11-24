from math import ceil

class Solution:

    NUMS = {"1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five",
            "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}
    TEENS = {"10": "Ten", "11":"Eleven", "12":"Twelve", "13": "Thirteen",
             "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen",
             "18": "Eighteen", "19": "Nineteen"}
    TENS = {"2": "Twenty", "3": "Thirty", "4": "Forty", "5": "Fifty",
            "6": "Sixty", "7": "Seventy", "8": "Eighty", "9": "Ninety"}
    PLACES = {4: "Trillion", 3: "Billion", 2: "Million", 1: "Thousand"}

    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"
        
        def convertTriplet(triplet: str):
            result = []
            if triplet[0] != "0":
                result.append(Solution.NUMS[triplet[0]])
                result.append("Hundred")
            if triplet[1:] in Solution.TEENS:
                result.append(Solution.TEENS[triplet[1:]])
            else:
                if triplet[1] != "0":
                    result.append(Solution.TENS[triplet[1]])
                if triplet[2] != "0":
                    result.append(Solution.NUMS[triplet[2]])
            return result
        
        s = str(num)
        s = s.zfill(ceil(len(s) / 3) * 3)
        result = []

        for i in range(len(s)//3):
            triplet = s[3*i:3*i+3]
            if triplet != "000":
                result.extend(convertTriplet(triplet))
                if i != len(s)//3 - 1:
                    result.append(Solution.PLACES[len(s)//3-i-1])

        return " ".join(result)
