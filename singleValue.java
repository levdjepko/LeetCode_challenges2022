class Solution {
    public int singleNumber(int[] nums) {
        HashMap <Integer, Integer> hm = new HashMap<>();
        int result = -1;
        for (int i = 0; i < nums.length; i++) {
            if (!hm.containsKey(nums[i])) {
                hm.put(nums[i], 1);
            } else {
                hm.put(nums[i], 2);
            }
        }
        for (int key: hm.keySet()) {
            if (hm.get(key) == 1) {
                result = key;
            }
        }
        return result;
    }
}
