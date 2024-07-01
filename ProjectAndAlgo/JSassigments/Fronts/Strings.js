// Remove Blanks
function removeBlanks(str) {
    let result = '';
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== ' ') {
            result += str[i];
        }
    }
    return result;
}

// Get Digits
function getDigits(str) {
    let result = '';
    for (let i = 0; i < str.length; i++) {
        if (!isNaN(Number(str[i]))) {
            result += str[i];
        }
    }
    return Number(result);
}

// Acronyms
function acronym(str) {
    let words = str.split(' ');
    let result = '';
    for (let i = 0; i < words.length; i++) {
        if (words[i].length > 0) {
            result += words[i][0].toUpperCase();
        }
    }
    return result;
}

// Count Non-Spaces
function countNonSpaces(str) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== ' ') {
            count++;
        }
    }
    return count;
}

// Remove Shorter Strings
function removeShorterStrings(arr, value) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].length >= value) {
            result.push(arr[i]);
        }
    }
    return result;
}

// Test cases
console.log(removeBlanks(" Pon derr oje a muzi k sena cmen de"));


console.log(getDigits("abc8c0d1ngd0j0!8"));
console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"));

console.log(acronym("ku ka uj mi ca uji"));

console.log(countNonSpaces("Oh God there is an error in line -1"));
console.log(countNonSpaces("Hello world !   "));

console.log(removeShorterStrings(['mire mengjess', 'rrezedrite', 'ajo', 'plutos', 'flas', 'mirupafshim'], 4));
console.log(removeShorterStrings(["I'm", 'having', 'trouble', 'pushing', 'to', 'git', 'hellpppppppppp'], 3));