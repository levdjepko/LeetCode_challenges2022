public int[] twoSum(int[] nums, int target) {
        int [] results = {0,0};
        boolean foundResult = false;

        // go over each item in an input array and get the sum of each pair of numbers
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if ((nums[i] + nums[j]) == target && !foundResult) {
                    results[0] = i;
                    results[1] = j;
                    foundResult = true;
                    break;
                }
            }
        }
        return results;
    }
