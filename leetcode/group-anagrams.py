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

    const anagrams = new Map();

    for (const str of strs) {
        const chars = str.split("");
        chars.sort();
        const key = JSON.stringify(chars)
        if (!anagrams.has(key)) {
            anagrams.set(key, [str]);
        } else {
            anagrams.get(key).push(str);
        }
    }
    return Array.from(anagrams.values())

    

};