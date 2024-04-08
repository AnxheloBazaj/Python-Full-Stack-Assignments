// version 1
var product = 1;
for (var i = 1; i <= 12; i++) {
    product *= i
}
console.log(product)
// version 2
product = 1;
for (var i = 12; i >= 1; i--) {
    product *= i
}
console.log(product)