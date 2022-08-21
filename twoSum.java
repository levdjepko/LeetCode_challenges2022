public int[] twoSum(int[] nums, int target) {
        int [] results = {0,0};
        for (int i = 0; i < nums.length; i++) {
            for (int j = 1; j < nums.length; j++) {
                if ((nums[i] + nums[j]) == target) {
                    results[0] = i;
                    results[1] = j;
                    break;
                }
            }
        }
        return results;
    }
