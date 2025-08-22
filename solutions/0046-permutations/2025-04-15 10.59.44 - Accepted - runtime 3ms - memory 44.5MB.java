class Solution {

    public List<List<Integer>> permuteN(int[] nums, int n) {
        if (n == 0)
            return new ArrayList<>(List.of(new ArrayList<>()));
    
        List<List<Integer>> perms = new ArrayList<>();

        for (List<Integer> perm : permuteN(nums, n-1)) {
            for (int num : nums) {
                if (!perm.contains(num)) {
                    List<Integer> newPerm = new ArrayList<>(perm);
                    newPerm.add(num);
                    perms.add(newPerm);
                }
            }
        }
        
        return perms;
    }

    public List<List<Integer>> permute(int[] nums) {
        return permuteN(nums, nums.length);
    }
}