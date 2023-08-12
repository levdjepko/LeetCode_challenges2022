public class Solution {
    public bool IsAnagram(string s, string t) {
        bool result = true;
        Hashtable hash = new Hashtable();
        if (s.Length != t.Length){
            result = false;                    
        }
        foreach (char c in s) {
            if (!hash.Contains(c)) {
                // add the key from original string
                hash.Add(c, 1);
            } else {
                int counter = (int)hash[c];
                hash[c] = counter + 1;
            }
        }
        
        foreach (char c in t){
            // if any of the letters is missing or the count is wrong, set result to false and break
            if (hash.Contains(c)){
                int counter = (int)hash[c];
                if (counter <= 0){
                    result = false;
                    break;
                } else {
                    hash[c] = counter - 1;
                }
            } else {
                result = false;
                    break;
            }
        }
        return result;
    }
}
