function pizzaOven(dough, crustType, sauceType, cheeses, toppings){
    var pizza={}
    pizza.dough = dough;
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
    
}
// rember that in order for our randomPizza function to work we have to pass lists of ingredients for each of the arguments
function randomPizza(dough, crustType, sauceType, cheeses, toppings){
    var randomPizza={}
    randomPizza.dough = dough[ Math.floor(Math.random() * dough.length )]
    randomPizza.crustType = crustType[ Math.floor(Math.random() * crustType.length )]
    randomPizza.sauceType = sauceType[ Math.floor(Math.random() * sauceType.length )]
    randomPizza.cheeses = cheeses[ Math.floor(Math.random() * cheeses.length )]
    randomPizza.toppings = toppings[ Math.floor(Math.random() * toppings.length )]
    return randomPizza;
}

console.log( "Custom ing piza", pizzaOven("sourdough", "stuffed", "alacrema", "mozzarella", ["spinach", "peperonni"]))
console.log( "Random ing piza", randomPizza(["sourdough","wheat", "corn"], ["deep dish", "dish deep", "stuffed", "stuffed2", "stuffed3"], ["traditional", "wosterschire", "diabolo"], [["mozzarella", "mozzarella2"], ["gouda", "swiss"],["gouda2", "swiss2"]],[["pepperoni", "sausage"],["peperoni", "sausage", "roukola"]]))


