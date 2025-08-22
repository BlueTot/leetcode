/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumNumbers(TreeNode root) {
        return sumNumbersFromNode(root, "");
    }

    private int sumNumbersFromNode(TreeNode curr, String numStr) {
        if (curr.left == null && curr.right == null) {
            return Integer.parseInt(numStr + curr.val);
        }
        
        int total = 0;
        if (curr.left != null)
            total += sumNumbersFromNode(curr.left, numStr + curr.val);
        if (curr.right != null)
            total += sumNumbersFromNode(curr.right, numStr + curr.val);
        return total;
    }
}