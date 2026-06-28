class Solution {
    public int missingNumber(int[] nums) {
        // Nums has n integers
        // Range of nums is 0 to n 
        // Find the single number missing in nums
        int missingNum = 0;
        // Sort array in ascending order to simplify this
        Arrays.sort(nums);
        //Iterate through nums
        for (int i=0; i<nums.length; i++) {
            // Check i against the number. The first i not to match is the number that's missing
            if (i!=nums[i]) {
                missingNum = i;
                return missingNum;
            }
        }
        // If the thing has reached here, it likely means that all the nums
        // until n are present, except n itself
        missingNum = nums.length;
        return missingNum;
    }
}
