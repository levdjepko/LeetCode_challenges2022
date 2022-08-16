public class Solution {
    public int Search(int[] nums, int target) {
        if (nums.Length == 1) {
            if (target == nums[0]){
                return 0;
            }
            else {
                return -1;
            }
        } else if (nums.Length == 2) {
            if(target == nums[0]){
                return 0;
            }
            else if (target == nums[1]) {
                return 1;
            }
            else {
                return -1;
            }
        }
        int start = 0;
        int end = nums.Length;
        int middle = nums.Length/2;
            //Console.WriteLine($"{start}, {middle}, {end}");
        int found = 0;
        if (target == nums[start]) {
            return start;
        }
        else if (nums[end-1] == target) {
            return end-1;
        }
        while (found == 0 && (end - start) >= 2) {
                if (target < nums[middle]) {
                    end = middle;
                    middle = (start + end) / 2;
                    Console.WriteLine($"{start}, {middle}, {end}");
                }
                else if (target == nums[middle]) {
                    found = 1;                    
                }
                else if (target > nums[middle]) {
                    start = middle;
                    middle = (start + end) / 2;
                    Console.WriteLine($"{start}, {middle}, {end}");
                }
        }
        if (found == 1) {
            return middle;
        }
        else  return -1;
    }
}
