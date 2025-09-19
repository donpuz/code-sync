/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    // map - "eat" --> ["ate", "eat", "tea"]
    // first decide how to set key, then to insert need to decide how to compare
    // idea: maybe sort each string while processing, then do string equality?
    // another idea: while processing, create map for each string and then do map equality
    // return values of map after

    // sort then compare approach
    // {{a: 0, b: 1, c: 2, ...}: ["ccb", "bcc"] }

    // 26 len arr and then serialize and the use that as the key

    const anagrams = new Map();

    for (const str of strs) {
        const freq = new Array(26).fill(0);
        // add to frequency array

        for (const char of str) {
            freq[char.charCodeAt(0) - 97] += 1;
        }
        const key = JSON.stringify(freq)
        if (!anagrams.has(key)) {
            anagrams.set(key, [str]);
        } else {
            anagrams.get(key).push(str);
        }
    }
    return Array.from(anagrams.values())

    

};