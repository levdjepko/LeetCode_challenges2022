public int MaximumWealth(int[][] accounts) {
        int maxW = 0;
        int currentW = 0;
        for (int i = 0; i < accounts.Length; i++) {
            for (int j = 0; j < accounts[i].Length; j++) {
                currentW += accounts[i][j];
            }
            if (currentW >= maxW) {
                maxW = currentW;
            } 
            currentW = 0;
        }
        return maxW;
    }
