/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // parse out the characters (remove non alphanumeric)
    // p1 starts from the beginning
    // p2 starts at the end
    // iterate over len/2 from the beginning and end using p1 and p2 and then compare

    // regex for the first step?
    const alphanumerics = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    for (let i = 0; i < alphanumerics.length / 2; i++) {
        // p1 = i
        // p2 = len - 1 - i

        if (alphanumerics[i] !== alphanumerics[alphanumerics.length - 1 - i]) {
            return false;
        }
    }
    return true;
};