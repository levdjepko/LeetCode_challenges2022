        int i = digits.length - 1;
        
        while (i >= 0 && digits[i] == 9) {
            digits[i] = 0;
            i--;
        }
        
        if (i >= 0){
            digits[i] = digits[i] + 1;
            return digits;
        }
        
        int[] results = new int[digits.length + 1];
        results[0] = 1;
        return results;
