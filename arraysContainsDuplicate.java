int[] nums = {1,2,3,4,5,6};
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i+1]){
                return true;
            }
        }
        return false;
