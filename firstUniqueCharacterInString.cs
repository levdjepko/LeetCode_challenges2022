public class Solution {
    public int FirstUniqChar(string s) {
        Dictionary<char,int> hs = new Dictionary<char,int>();
    for (int i = 0; i < s.Length; i++)
    {
        if (!hs.ContainsKey(s[i]))
        {
            hs.Add(s[i], i); // now we have a dictionary item like this: --- unique char --- its index ---
        } else
        {
            hs[s[i]] = -1; // Here we replace the real index with -1 as this can't be an answer
        }
    }
    // iterate over the dictionary again and find the first non -1 item
    foreach (var item in hs.Keys)
    {
        var value = hs[item];
        if (value != -1)
        {
            return value;            
        }
    }
    return -1;
    }
}
