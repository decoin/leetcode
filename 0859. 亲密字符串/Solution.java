class Solution {
    public boolean buddyStrings(String A, String B) {
        if (A.length() != B.length()){
            return false;
        }
        if (A.equals(B)){
            Set<Character> set = new HashSet<>();
            for (int i = 0;i < A.length(); i++){
                set.add(A.charAt(i));
            }
            return set.size() == A.length() ? false : true;
        }
        char[] charsA = A.toCharArray();
        char[] charsB = B.toCharArray();
        int[] diff = new int[2];
        int k = 0;
        for (int i = 0; i < charsA.length; i++) {
            if (charsA[i] != charsB[i]) {
                if (k > 1) {
                    return false;
                }
                diff[k++] = i;
            }
        }
        if (k == 2 && charsA[diff[0]] == charsB[diff[1]] && charsA[diff[1]] == charsB[diff[0]]) {
            return true;
        } else {
            return false;
        }
    }
}
