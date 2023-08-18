
using System.Text.RegularExpressions;

Console.WriteLine(IsPalindrome("AA22AA $.  -- __"));

 bool IsPalindrome(string s)
{
    string cleanedString = Regex.Replace(s, "[^a-zA-Z0-9]+", "").ToLower();
    Console.WriteLine(cleanedString);
    for (int i = 0; i < cleanedString.Length / 2; i++)
    {
        // iterate over every character and compare it to its mirrored character on the other side of the same string
        if (cleanedString[i] == cleanedString[cleanedString.Length - 1 - i])
        {
            // characters match, all good so far
        } else
        {
            return false;
        }
    }    
    return true;
}
