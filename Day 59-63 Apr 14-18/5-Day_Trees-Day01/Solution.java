import java.util.*;

// Assume the student provides complete implementations of each method below.
public class Solution {

    // Definition for a binary tree node.
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int x) { this.val = x; }
    }

    // ======================= Binary Trees (BT) Methods =======================

    // 1. Boundary Traversal: Returns a list of node values along the boundary.
    public static List<Integer> boundaryTraversal(TreeNode root) {
        // STUDENT IMPLEMENTATION HERE
        return new ArrayList<>();  
    }

    // 2. Vertical Order Traversal: Returns a list of lists grouped vertically.
    public static List<List<Integer>> verticalOrderTraversal(TreeNode root) {
        // STUDENT IMPLEMENTATION HERE
        return new ArrayList<>();
    }

    // 3. Bottom View: Returns the bottom view (left to right) of the tree.
    public static List<Integer> bottomView(TreeNode root) {
        // STUDENT IMPLEMENTATION HERE
        return new ArrayList<>();
    }

    // 4. Sum of Nodes at Kth Level: Returns the sum of node values at depth k.
    public static int sumAtKthLevel(TreeNode root, int k) {
        // STUDENT IMPLEMENTATION HERE
        return 0;
    }

    // ======================= Binary Search Trees (BST) Methods =======================

    // 5. Check if BST is Full: Returns true if every node has either 0 or 2 children.
    public static boolean isFullBST(TreeNode root) {
        // STUDENT IMPLEMENTATION HERE
        return false;
    }

    // 6. Second Largest Element: Returns the second largest node value.
    public static Integer secondLargest(TreeNode root) {
        // STUDENT IMPLEMENTATION HERE
        return null;
    }

    // 7. Floor and Ceil of a Value: Returns an array {floor, ceil}. Use -1 if none exists.
    public static int[] floorCeil(TreeNode root, int key) {
        // STUDENT IMPLEMENTATION HERE
        return new int[]{-1, -1};
    }

    // 8. Count Nodes within Range: Returns the count of nodes whose values lie in [low, high].
    public static int countNodesInRange(TreeNode root, int low, int high) {
        // STUDENT IMPLEMENTATION HERE
        return 0;
    }

    // ======================= Balanced Binary Search Trees (BBST) Methods =======================

    // 9. Construct Balanced BST from Sorted Array: Returns a balanced BST root.
    public static TreeNode constructBalancedBST(int[] sortedArray) {
        // STUDENT IMPLEMENTATION HERE
        return null;
    }

    // 10. AVL Tree Check: Returns true if the BST is AVL-balanced.
    public static boolean isAVL(TreeNode root) {
        // STUDENT IMPLEMENTATION HERE
        return false;
    }

    // 11. Delete Node from AVL Tree: Deletes key and returns the new AVL tree root.
    public static TreeNode deleteFromAVL(TreeNode root, int key) {
        // STUDENT IMPLEMENTATION HERE
        return null;
    }

    // 12. Convert BST to Balanced BST: Returns the balanced BST converted from the original.
    public static TreeNode convertToBalancedBST(TreeNode root) {
        // STUDENT IMPLEMENTATION HERE
        return null;
    }

    // ------------------------- Utility Methods -------------------------

    // For comparing two lists of integers.
    public static boolean listEquals(List<Integer> a, List<Integer> b) {
        if (a.size() != b.size()) return false;
        for (int i = 0; i < a.size(); i++) {
            if (!a.get(i).equals(b.get(i))) return false;
        }
        return true;
    }

    // For comparing two lists of lists of integers.
    public static boolean listOfListEquals(List<List<Integer>> a, List<List<Integer>> b) {
        if (a.size() != b.size()) return false;
        for (int i = 0; i < a.size(); i++) {
            if (!listEquals(a.get(i), b.get(i))) return false;
        }
        return true;
    }

    // Inorder traversal helper (to verify BST structure).
    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        inorderHelper(root, list);
        return list;
    }
    public static void inorderHelper(TreeNode root, List<Integer> list) {
        if (root == null) return;
        inorderHelper(root.left, list);
        list.add(root.val);
        inorderHelper(root.right, list);
    }

    // ------------------------- Test Methods -------------------------

    public static void testBoundaryTraversal() {
        System.out.println("Testing Boundary Traversal:");
        int passed = 0;
        // Test 1: Empty tree
        TreeNode root = null;
        List<Integer> result = boundaryTraversal(root);
        List<Integer> expected = new ArrayList<>();
        if (listEquals(result, expected)) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node tree
        root = new TreeNode(1);
        result = boundaryTraversal(root);
        expected = Arrays.asList(1);
        if (listEquals(result, expected)) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Tree with both left and right children
        //         1
        //        / \
        //       2   3
        //      / \   \
        //     4   5   6
        root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.left = new TreeNode(4); root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(6);
        result = boundaryTraversal(root);
        expected = Arrays.asList(1,2,4,5,6,3);
        if (listEquals(result, expected)) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Only left subtree
        //      1
        //     /
        //    2
        //   /
        //  3
        root = new TreeNode(1);
        root.left = new TreeNode(2); root.left.left = new TreeNode(3);
        result = boundaryTraversal(root);
        expected = Arrays.asList(1,2,3);
        if (listEquals(result, expected)) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Only right subtree
        // 1
        //  \
        //   2
        //    \
        //     3
        root = new TreeNode(1);
        root.right = new TreeNode(2); root.right.right = new TreeNode(3);
        result = boundaryTraversal(root);
        // (Assume right boundary is printed in reverse order)
        expected = Arrays.asList(1,3,2);
        if (listEquals(result, expected)) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Boundary Traversal Passed " + passed + "/5 tests\n");
    }

    public static void testVerticalOrderTraversal() {
        System.out.println("Testing Vertical Order Traversal:");
        int passed = 0;
        // Test 1: Empty tree
        TreeNode root = null;
        List<List<Integer>> result = verticalOrderTraversal(root);
        List<List<Integer>> expected = new ArrayList<>();
        if (listOfListEquals(result, expected)) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node
        root = new TreeNode(1);
        result = verticalOrderTraversal(root);
        expected = new ArrayList<>();
        expected.add(Arrays.asList(1));
        if (listOfListEquals(result, expected)) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Complex tree
        //         1
        //        / \
        //       2   3
        //      / \   \
        //     4   5   6
        root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.left = new TreeNode(4); root.left.right = new TreeNode(5);
        root.right.right = new TreeNode(6);
        result = verticalOrderTraversal(root);
        expected = new ArrayList<>();
        expected.add(Arrays.asList(4));
        expected.add(Arrays.asList(2));
        expected.add(Arrays.asList(1,5));
        expected.add(Arrays.asList(3));
        expected.add(Arrays.asList(6));
        if (listOfListEquals(result, expected)) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Left skewed tree
        //       1
        //      /
        //     2
        //    /
        //   3
        root = new TreeNode(1);
        root.left = new TreeNode(2); root.left.left = new TreeNode(3);
        result = verticalOrderTraversal(root);
        expected = new ArrayList<>();
        expected.add(Arrays.asList(3));
        expected.add(Arrays.asList(2));
        expected.add(Arrays.asList(1));
        if (listOfListEquals(result, expected)) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Right skewed tree
        root = new TreeNode(1);
        root.right = new TreeNode(2); root.right.right = new TreeNode(3);
        result = verticalOrderTraversal(root);
        expected = new ArrayList<>();
        expected.add(Arrays.asList(1));
        expected.add(Arrays.asList(2));
        expected.add(Arrays.asList(3));
        if (listOfListEquals(result, expected)) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Vertical Order Traversal Passed " + passed + "/5 tests\n");
    }

    public static void testBottomView() {
        System.out.println("Testing Bottom View:");
        int passed = 0;
        // Test 1: Empty tree
        TreeNode root = null;
        List<Integer> result = bottomView(root);
        List<Integer> expected = new ArrayList<>();
        if (listEquals(result, expected)) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node
        root = new TreeNode(1);
        result = bottomView(root);
        expected = Arrays.asList(1);
        if (listEquals(result, expected)) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Sample tree
        //         20
        //        /  \
        //       8    22
        //      / \     \
        //     5   3     25
        //        / \
        //       10 14
        root = new TreeNode(20);
        root.left = new TreeNode(8); root.right = new TreeNode(22);
        root.left.left = new TreeNode(5); root.left.right = new TreeNode(3);
        root.right.right = new TreeNode(25);
        root.left.right.left = new TreeNode(10); root.left.right.right = new TreeNode(14);
        result = bottomView(root);
        expected = Arrays.asList(5,10,3,14,25);
        if (listEquals(result, expected)) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Left skewed tree
        root = new TreeNode(1);
        root.left = new TreeNode(2); root.left.left = new TreeNode(3);
        result = bottomView(root);
        expected = Arrays.asList(3,2,1);
        if (listEquals(result, expected)) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Right skewed tree
        root = new TreeNode(1);
        root.right = new TreeNode(2); root.right.right = new TreeNode(3);
        result = bottomView(root);
        expected = Arrays.asList(1,2,3);
        if (listEquals(result, expected)) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Bottom View Passed " + passed + "/5 tests\n");
    }

    public static void testSumAtKthLevel() {
        System.out.println("Testing Sum of Nodes at Kth Level:");
        int passed = 0;
        // Test 1: Empty tree
        TreeNode root = null;
        int result = sumAtKthLevel(root, 2);
        int expected = 0;
        if (result == expected) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node at level 0
        root = new TreeNode(5);
        result = sumAtKthLevel(root, 0);
        expected = 5;
        if (result == expected) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Two level tree
        //      1
        //     / \
        //    2   3
        root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        result = sumAtKthLevel(root, 1);
        expected = 5;  // 2 + 3
        if (result == expected) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Deeper tree
        //         1
        //        / \
        //       2   3
        //      /
        //     4
        root = new TreeNode(1);
        root.left = new TreeNode(2); root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        result = sumAtKthLevel(root, 2);
        expected = 4;
        if (result == expected) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Level does not exist
        result = sumAtKthLevel(root, 5);
        expected = 0;
        if (result == expected) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Sum of Nodes at Kth Level Passed " + passed + "/5 tests\n");
    }

    public static void testIsFullBST() {
        System.out.println("Testing Check if BST is Full:");
        int passed = 0;
        // Test 1: Empty tree (assume empty tree is full)
        TreeNode root = null;
        boolean result = isFullBST(root);
        boolean expected = true;
        if (result == expected) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node
        root = new TreeNode(1);
        result = isFullBST(root);
        expected = true;
        if (result == expected) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Full BST: 
        //    2
        //   / \
        //  1   3
        root = new TreeNode(2);
        root.left = new TreeNode(1); root.right = new TreeNode(3);
        result = isFullBST(root);
        expected = true;
        if (result == expected) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Not full BST
        //    2
        //   /
        //  1
        root = new TreeNode(2);
        root.left = new TreeNode(1);
        result = isFullBST(root);
        expected = false;
        if (result == expected) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Larger tree with a missing child
        root = new TreeNode(4);
        root.left = new TreeNode(2); root.right = new TreeNode(6);
        root.left.left = new TreeNode(1);
        root.left.left.right = new TreeNode(15);  // extra node making it not full
        root.right.left = new TreeNode(5); root.right.right = new TreeNode(7);
        result = isFullBST(root);
        expected = false;
        if (result == expected) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Check if BST is Full Passed " + passed + "/5 tests\n");
    }

    public static void testSecondLargest() {
        System.out.println("Testing Second Largest Element:");
        int passed = 0;
        // Test 1: One node
        TreeNode root = new TreeNode(10);
        Integer result = secondLargest(root);
        Integer expectedVal = null;
        if ((result == null && expectedVal == null) || (result != null && result.equals(expectedVal))) {
            System.out.println("Test 1 Passed"); passed++;
        } else System.out.println("Test 1 Failed");

        // Test 2: Two nodes (root and right)
        root = new TreeNode(10); root.right = new TreeNode(20);
        result = secondLargest(root);
        expectedVal = 10;
        if (result != null && result.equals(expectedVal)) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Multiple nodes
        //      20
        //     /  \
        //   10   30
        //          \
        //           40
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.right = new TreeNode(30);
        root.right.right = new TreeNode(40);
        result = secondLargest(root);
        expectedVal = 30;
        if (result != null && result.equals(expectedVal)) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Largest node has a left subtree candidate
        //      20
        //     /
        //   10
        //     \
        //     15
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.left.right = new TreeNode(15);
        result = secondLargest(root);
        expectedVal = 15;
        if (result != null && result.equals(expectedVal)) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Largest node with left subtree
        //      20
        //     /  \
        //   10   30
        //        /
        //       25
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.right = new TreeNode(30);
        root.right.left = new TreeNode(25);
        result = secondLargest(root);
        expectedVal = 25;
        if (result != null && result.equals(expectedVal)) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Second Largest Element Passed " + passed + "/5 tests\n");
    }

    public static void testFloorCeil() {
        System.out.println("Testing Floor and Ceil of a Value:");
        int passed = 0;
        // Test 1: Empty tree
        TreeNode root = null;
        int[] resultArr = floorCeil(root, 15);
        int[] expectedArr = new int[]{-1, -1};
        if (Arrays.equals(resultArr, expectedArr)) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node equal to key
        root = new TreeNode(15);
        resultArr = floorCeil(root, 15);
        expectedArr = new int[]{15,15};
        if (Arrays.equals(resultArr, expectedArr)) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Key between nodes
        //      20
        //     /  \
        //   10    30
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.right = new TreeNode(30);
        resultArr = floorCeil(root, 25);
        expectedArr = new int[]{20,30};
        if (Arrays.equals(resultArr, expectedArr)) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Key less than smallest
        resultArr = floorCeil(root, 5);
        expectedArr = new int[]{-1,10};
        if (Arrays.equals(resultArr, expectedArr)) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Key greater than largest
        resultArr = floorCeil(root, 35);
        expectedArr = new int[]{30,-1};
        if (Arrays.equals(resultArr, expectedArr)) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Floor and Ceil of a Value Passed " + passed + "/5 tests\n");
    }

    public static void testCountNodesInRange() {
        System.out.println("Testing Count Nodes within Range:");
        int passed = 0;
        // Test 1: Empty tree
        TreeNode root = null;
        int result = countNodesInRange(root, 10, 20);
        int expected = 0;
        if (result == expected) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node inside range
        root = new TreeNode(15);
        result = countNodesInRange(root, 10, 20);
        expected = 1;
        if (result == expected) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Single node outside range
        root = new TreeNode(25);
        result = countNodesInRange(root, 10, 20);
        expected = 0;
        if (result == expected) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Larger tree
        //         20
        //        /  \
        //       10   30
        //      /  \
        //     5   15
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.right = new TreeNode(30);
        root.left.left = new TreeNode(5); root.left.right = new TreeNode(15);
        result = countNodesInRange(root, 10, 20);
        expected = 3; // (10,15,20)
        if (result == expected) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: All nodes in range
        result = countNodesInRange(root, 0, 40);
        expected = 5;
        if (result == expected) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Count Nodes within Range Passed " + passed + "/5 tests\n");
    }

    public static void testConstructBalancedBST() {
        System.out.println("Testing Construct Balanced BST from Sorted Array:");
        int passed = 0;
        // Test 1: Empty array
        int[] arr = new int[]{};
        TreeNode root = constructBalancedBST(arr);
        List<Integer> inorder = inorderTraversal(root);
        if (inorder.isEmpty()) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single element
        arr = new int[]{10};
        root = constructBalancedBST(arr);
        inorder = inorderTraversal(root);
        if (inorder.equals(Arrays.asList(10))) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Two elements
        arr = new int[]{5,10};
        root = constructBalancedBST(arr);
        inorder = inorderTraversal(root);
        if (inorder.equals(Arrays.asList(5,10))) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Multiple elements
        arr = new int[]{1,2,3,4,5,6,7};
        root = constructBalancedBST(arr);
        inorder = inorderTraversal(root);
        if (inorder.equals(Arrays.asList(1,2,3,4,5,6,7))) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Non continuous sorted array
        arr = new int[]{2,5,8,10,13};
        root = constructBalancedBST(arr);
        inorder = inorderTraversal(root);
        if (inorder.equals(Arrays.asList(2,5,8,10,13))) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Construct Balanced BST Passed " + passed + "/5 tests\n");
    }

    public static void testIsAVL() {
        System.out.println("Testing AVL Tree Check:");
        int passed = 0;
        // Test 1: Empty tree is AVL
        TreeNode root = null;
        if (isAVL(root) == true) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Single node is AVL
        root = new TreeNode(10);
        if (isAVL(root) == true) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Balanced BST is AVL
        //      10
        //     /  \
        //    5   15
        root = new TreeNode(10);
        root.left = new TreeNode(5); root.right = new TreeNode(15);
        if (isAVL(root) == true) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Not AVL (unbalanced)
        //      10
        //     /
        //    5
        //   /
        //  2
        root = new TreeNode(10);
        root.left = new TreeNode(5); root.left.left = new TreeNode(2);
        if (isAVL(root) == false) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: More complex unbalanced tree
        //      30
        //     /
        //   20
        //     \
        //     25
        root = new TreeNode(30);
        root.left = new TreeNode(20); root.left.right = new TreeNode(25);
        if (isAVL(root) == false) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("AVL Tree Check Passed " + passed + "/5 tests\n");
    }

    public static void testDeleteFromAVL() {
        System.out.println("Testing Delete Node from AVL Tree:");
        int passed = 0;
        // Test 1: Delete from empty tree
        TreeNode root = null;
        root = deleteFromAVL(root, 10);
        if (root == null) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Delete a leaf node
        //      20
        //     /  \
        //   10   30
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.right = new TreeNode(30);
        root = deleteFromAVL(root, 10);
        List<Integer> inorder = inorderTraversal(root);
        if (inorder.equals(Arrays.asList(20,30))) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Delete root node with two children
        //      20
        //     /  \
        //   10   30
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.right = new TreeNode(30);
        root = deleteFromAVL(root, 20);
        inorder = inorderTraversal(root);
        if (inorder.equals(Arrays.asList(10,30))) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Delete node causing unbalance
        //      30
        //     /  \
        //   20   40
        //   /
        // 10
        root = new TreeNode(30);
        root.left = new TreeNode(20); root.right = new TreeNode(40);
        root.left.left = new TreeNode(10);
        root = deleteFromAVL(root, 40);
        inorder = inorderTraversal(root);
        if (inorder.equals(Arrays.asList(10,20,30))) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: Delete non-existing node
        root = new TreeNode(30);
        root.left = new TreeNode(20); root.right = new TreeNode(40);
        List<Integer> original = inorderTraversal(root);
        root = deleteFromAVL(root, 50);
        inorder = inorderTraversal(root);
        if (inorder.equals(original)) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Delete Node from AVL Tree Passed " + passed + "/5 tests\n");
    }

    public static void testConvertToBalancedBST() {
        System.out.println("Testing Convert BST to Balanced BST:");
        int passed = 0;
        // Test 1: Empty tree
        TreeNode root = null;
        root = convertToBalancedBST(root);
        if (root == null) { System.out.println("Test 1 Passed"); passed++; }
        else System.out.println("Test 1 Failed");

        // Test 2: Already balanced tree
        //      20
        //     /  \
        //   10   30
        root = new TreeNode(20);
        root.left = new TreeNode(10); root.right = new TreeNode(30);
        TreeNode balanced = convertToBalancedBST(root);
        List<Integer> inorderOrig = inorderTraversal(root);
        List<Integer> inorderBalanced = inorderTraversal(balanced);
        if (inorderOrig.equals(inorderBalanced)) { System.out.println("Test 2 Passed"); passed++; }
        else System.out.println("Test 2 Failed");

        // Test 3: Unbalanced tree conversion
        //      10
        //        \
        //        20
        //          \
        //          30
        root = new TreeNode(10);
        root.right = new TreeNode(20); root.right.right = new TreeNode(30);
        balanced = convertToBalancedBST(root);
        inorderBalanced = inorderTraversal(balanced);
        if (inorderBalanced.equals(Arrays.asList(10,20,30))) { System.out.println("Test 3 Passed"); passed++; }
        else System.out.println("Test 3 Failed");

        // Test 4: Larger unbalanced tree
        int[] arr = new int[]{1,2,3,4,5,6,7,8,9};
        root = constructBalancedBST(arr);
        // Deliberately unbalance: attach extra node on rightmost branch
        TreeNode temp = root;
        while(temp.right != null) { temp = temp.right; }
        temp.right = new TreeNode(10);
        balanced = convertToBalancedBST(root);
        inorderBalanced = inorderTraversal(balanced);
        if (inorderBalanced.equals(Arrays.asList(1,2,3,4,5,6,7,8,9,10))) { System.out.println("Test 4 Passed"); passed++; }
        else System.out.println("Test 4 Failed");

        // Test 5: BST with duplicate values (if allowed)
        arr = new int[]{1,2,2,3,4};
        root = constructBalancedBST(arr);
        balanced = convertToBalancedBST(root);
        inorderBalanced = inorderTraversal(balanced);
        if (inorderBalanced.equals(Arrays.asList(1,2,2,3,4))) { System.out.println("Test 5 Passed"); passed++; }
        else System.out.println("Test 5 Failed");

        System.out.println("Convert BST to Balanced BST Passed " + passed + "/5 tests\n");
    }

    // ------------------------- Main Method -------------------------
    public static void main(String[] args) {
        testBoundaryTraversal();
        testVerticalOrderTraversal();
        testBottomView();
        testSumAtKthLevel();
        testIsFullBST();
        testSecondLargest();
        testFloorCeil();
        testCountNodesInRange();
        testConstructBalancedBST();
        testIsAVL();
        testDeleteFromAVL();
        testConvertToBalancedBST();
    }
}
