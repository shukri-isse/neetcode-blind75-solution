class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        //convert strings into char arrays
        const charArrS = s.split("");
        const charArrT = t.split("");
        // console.log(`charArrS: ${charArrS}`);
        // console.log(`charArrT: ${charArrT}`);

        // sort each char array
        const sortedS = charArrS.sort();
        const sortedT = charArrT.sort();

        //check if joined arrays/strings are equal
        return sortedS.join('') === sortedT.join('');
    }
}