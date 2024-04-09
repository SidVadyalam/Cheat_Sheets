alert("I am god"); /* This is pretty inefficient becuase it blocks the running of the 
rest of the program. Instead we use the console */

console.log("Hello World"); /* This outputs to the console */
/* Log is a method that runs off the console object */

console.error("This is an error") /* This produces an error in the console */

console.warn("This gives a warning") /* This produces a warning in the console */

let variable;
variable = 50;
variable = 90;
console.log(variable);

const constant = 3.1415;
console.log(constant);


/* Defining Variables */

/* There are 3 ways to define variables in JavaScript: 
1. Using var
2. Using let
3. Using const

1. var will produce a variable with global scope. It is not advisable to use var since it's use is pretty rare.
2. let produces a variable with local scope. It is more commonly used, and the value of the variable can be changed,
3. const will produce a variable with a constant value. a variable being declared with const will not change it's value, and cannot be changed. */

const text = 'John' // String variable
// Semicolons not necessary, but good habit

const num = 40;
const deci = 4.5; // Both are Number variables

const bool = true; // Boolean variable

const empty = null; // null value variable

const unknown = undefined; 
let x; // Both are variables of undefined/unknown datatype

console.log(typeof num); // Returns Datatype of variable

console.log(typeof empty); // This return object instead of null. This is due to a glitch in JavaSript


/* Datatypes in JS */

/* Below are the Primitive Datatypes in JS 

String, Numbers, Boolean, null, undefined, Symbol

The last one is pretty rarely used and was introduced long back, so don't worry about it */


console.log("My name is " + text + " and I am " + num + "years old"); // This is the old way of string concatenation, that is used pretty rarely

console.log(`My name is ${text} and I am ${num} years old`); // This is the new modern and better way to concatenate

const hello = `My name is ${text} and I am ${num} years old`; // You can even save this concatenated string

/* Concatenation */

const s = "Sample String";

console.log(s.length); // This returns the length of the String
// Because .length is a property, not a method, we do not keep parenthesis () next to it. Only methods have parentheisis.

console.log(s.toUpperCase()); // This returns the upper case version of the string. This is a method unlinke .length

console.log(s.toLowerCase()); // This returns the lower case version of the string. This is a method unlinke .length

console.log(s.substring(0, 5)); // This returns a substring, staring from index of the first number, and upto but not including index of the last number index

console.log(s.substring(0,9).toUpperCase()); // We can even chain together multiple methods

console.log(s.split('')); // This methord splits a string into an array. Depending on the parameter, we can split the string differet ways.
// The empty string parameter splits it along every letter i.e every element of the index is a letter

console.log(s.split(' ')); // This parameter will split the array at every instance of the specified character. Eg: "Hello world" will split as ["Hello", "world"]


/* String methods and properties */

// There are 2 ways to create and array

const numbers = new Array(1,2,3,4,5,6); // This is how you create an Array. The syntax here shows the constructor for object array. There also is another more efficient to create one.

console.log(numbers);

const fruits = ["apples", "oranges", "pears"]; // This is another way to create an Array.

const datatype = ["String", 3.14, true, [8,9,0,9]]; // In Java script, it is possible to create arrays with multiple datatypes. There is also no need to define the length of 
// the array like in Java

console.log(fruits[1]); // We can acess a certain element in an array, by simply referencing it's index as shown. Like all programming languages, array indexes start from 0.

fruits[3] = "grapes"; // We can append values to an array by assiging the latest index to a desired value. Now even though the array is declared as a const, 
// we can still make changes to the array, such as adding values. The only thing that we can't do is reassign an array to new values. 

fruits.push("watermelon"); // This is another way of adding values to the end of an array. This method 'pushes' values onto the end of the array

fruits.unshift("strawberries"); // This method adds an element to the beginning of an Array.

fruits.pop(); // This method removes the last elemnt of an array. Kinda like python

console.log(Array.isArray(fruits)); // This method return true if the parameter is an array. It is part of the Array object

console.log(fruits.indexOf("strawberries")); // This method returns the index of the paramenter in the array.

console.log(fruits);

/* Arrays */


const person = { // This is how you create an object literal.
	firstName: "John",
	lastName: "Doe",
	age: 50,
	hobbies: ["music", "movies", "sports"],
	address: {  // You can even include/embed object literals in object literals.
		street: "50 main",
		city: "boston",
		state: "MA"
		}
	}

console.log(person.firstName); // This is how you acess a value in an object. Note: if we were to use alert function, we would bot see proper output

console.log(person.firstName, person.lastName); // You can also output multiple things to console if you seperate them by a comma

console.log(person.hobbies[1]); // This is how you acess an element in an array that itself is in an object

console.log(person.address.city); // This is how you acess an element of an object literal that itself is in an object literal

const { firstName, lastName } = person; // We can also make the elements in the object literal variables with this syntax. Note: the equals 
// to sign here does not represent assignment, it represents object literal elemnets being pulled out of the object literal

console.log(firstName);

const { address: {city}} = person; // This is how you extract an element in an embedded object and declare it as an array

person.isHappy = true; // This is how you add properties to an existing object literal

/* Object Literals */

const toDos = [ // This is how you create an array of objects
{
	id: 1,
	text: "take out trash",
	isCompleted: true
},
{
	id: 2,
	text: "Meeting with Boss",
	isCompleted: true
},
{
	id: 3,
	text: "Denitst Appointment",
	isCompleted: false
},


	]

console.log(toDos[0].text); // This prints out an element of an object that is part of an array

/* JSON is a data format (a way that data is presented) that is used in full stack development. When ever you send data to a server,
 you send it in JSON format. Only if you send it in this format will the server be able to interpret your data. The server also send you data back in this format.
 The format of JSON is kinda like a bunch of objects in arrays in JS*/

const toDosJSON = JSON.stringify(toDos); // This is how you convert normal javascript to JSON

console.log(toDosJSON);

/* Arrays of objects*/


/* For loop */

for(let i = 0; i < 10; i ++){ // This is how you write a for loop. The first part is variable declaration; second part is condition; third is increment
	console.log(`For Loop Number ${i}`);
}


/* While loop */

let i = 0;
while( i < 10){
	console.log(`While Loop Number ${i}`);
	i ++;
}

/* For loops with Arrays */

for(let i = 0; i < toDos.length; i ++){
	console.log(toDos[i].text);

}

/* For - of Loop */

for(let i of toDos){ // This is a for of loop, just like the one in Java
	console.log(i.text);
};
/* Loops */


toDos.forEach(function(a){ // This is the forEach methord for the array. This method produces an output that is similar to the for of loop.
// This method takes a function as a parameter, and then a variable name for the paramenter of the function (This variable name is similar to the variable name in the for of loop).
// The method then loops through each value in the array and stores it in the variable provided, kinda like a for of loop.
	console.log(a.text);
});

const toDosText = toDos.map(function(a){ // This is the map method. This method also takes a function as an input and is similar to the previous method, but unlike the previous methord it returns an output. This output that it returns is
// another array, consisting of whaterever we specify using the return keyword. It is important to save the return value of this method in a variable for later use.
	return a.text;
});

console.log(toDosText);

const toDosisCompleted = toDos.filter(function(a){ // This is the filter method. This method is similar to the previous two array methods. This method loops through the array, and returns another array
// that consists of object whose elements satisfy the given condition that is placed next to the return statement. This method also gives a return value of an array, so besure to store it in an array.
	return a.isCompleted === true;
})

console.log(toDosisCompleted);

const b = toDos.filter(function(a){ // We can even chain together methods as shown
	return a.isCompleted === true;
}).map(function(a){
	return a.text;
})

console.log(b);

/* Higher order Array Methods */ 

const c = "10";

// This is the basic if statement in JS

if (c == 10){ // The double equals to here checks if the value on either side of the equality are the same regardless of the datatype. So in this case, the if statement will execute depite x holding the string value of 10 not number 
	console.log("c is 10");
}

if (c === 10){ // This thriple equals to here checks if the values to either side of the equality are the same considering the datatype i.e the value and the datatype of the things on either side are the same
	console.log("c is 10"); 
} else { // This is how you add an else statement
	console.log("c is NOT 10");
}

if ( c === 10){
	console.log("c is 10");
} else if (c > 10){ // This is how you add if else statements
	console.log("c is greater than 10")
} else{
	console.log("c is less than 10")
}

const a = 1;
const d = 2;

if (a > 2 || d === 2){ // This is how you write the or boolean operator
	console.log("a is greater than 2 or d is equal to 2");
}

if ( a === 1 && d === 2){ // This is how you write the and boolean operator
	console.log("a is equal to one and d is equal to 2");
}

// There is a shortcut to assigning variables values based on conditions. Instead of using if statements then a declaration, we can directly assign variables values based on a condition and do that
// in a single line. We can do this with the help of an operator called the ternary operator. The ternary operator acts like a "then" statement in english. If a condition is true "then" (ternary operator)
// it assigns a variable our specified value. The symbol for ternary operator is the question mark ?

const color = (c > 10) ? "red" : "blue"; // The semicolon in the statement here reads as else.
// The statement above uses the ternary operator in action. It reads, if c is greater than 10 (condition) then (ternary operator) has value of "red" (first value) else (colon) it has a value of "blue" (second alternate value) 

console.log(color);

// There is one final way we can apply conditionals to our code, and that is by using the switch function. The switch function is basically the Case.. of .. otherwise conditional that uou learned in IGCSE
// Basically the switch function takes a variable as input then compares the value of the variable to different cases. If the variable's stored value matches one of the specified cases, then the following code gets extecuted.
// if it does not match, then the default code gets executed. It is also important to write break after each case, or else the default code will be executed every single time.


switch(color){
case "red":
	console.log("color is red");
	break;
case "blue":
	console.log("color is blue");
	break;
default:
	console.log("color is NOT red or blue");
}


/* Conditionals */

function addnum(num1, num2) { // We can define our own functions in JS using this syntax. Remeber to specify the function keyword in our program. The parameters for our function go in the brackets
	console.log(num1 + num2);
}

addnum(); // If we call a function without parameters, we wil get NaN error. NaN stands for not a number, and this error occurs because the parameters aren't given any values
// despite the function being defined with parameters

function subnum (num1 = 1, num2 = 3){
	console.log(num1 - num2);
} // We can also define default values to parameters by assigning them default values during the function definition.

subnum(); // Since there are no parameters here, the funnction will execute with the default values.

function multnum(num1, num2){ // We can also keep a return value to functions as show here
	return num1*num2;
}

console.log(multnum(5, 8));

/* Functions */

// Arrow functions are fuctions that are defined used a special syntax. They are no different than any normal function, but they do save us some lines of code when we define them
// They are a relatively new introduction and their syntax is a bit unique
// We define arrow functions kinda like how we define variables, we also do not use the keyword functions when defining them


const divnum = (num1 = 1, num2 = 1) => {
	return num1 / num2;
}

// We can even omit the curly braces and the return statement if our function code is only one statement

const addsubnum = (num1 = 1, num2 = 1, num3 = 0) => num1 + num2 - num3;

// If we have one parameter, then we don't even need the parenthesis

const addfive = num1 => num1 + 5;

// We can even use arrow functions as input to the array methods above

/* Arrow functions */

// We have seen how to make object literals, however there are also other ways of creating objects.
// We can create objects using a constructor function, and this is shown here below
// A construction function does not instantiate an object, it is simply a function that tells how to instantiate an object

function Person(firstName, lastName, dob){ // To create an object, we use the function keyword, followed by the name of our object. When naming objects, always use a capital letter
// this helps JS know that what we defined is an object not a function. Then in the parenthesis, keep the names of your object properties. Once that is done, use the 'this' keyword to assign properties their values as shown below.
	this.firstName = firstName;
	this.lastName = lastName;
	this.dob = new Date(dob); // There is a default date object constructor in JS, and this is how you specify it.
	this.getBirthYear = function(){ // We can even set up methods within our object constructor function as shown.
		return this.dob.getFullYear();
	}
}

// Now that we have defined the constructor function for the object. We need to create or instantiate an object. This can be done by passing the constructor function values, and storing it in a variable.

const person1 = new Person("Joe", "Douglass", "4-3-1980");
const person2 = new Person("Mary", "Smith", "3-6-1950");

// Here we have two objects created

console.log(person1);
console.log(person2.firstName);
console.log(person1.getBirthYear())
console.log(person1.dob.getFullYear()); // Since dates in JS are represented as objects, they can have methods that allow you to manipulate them. The get full year method returns the full year part of the date

// If we want to edit an object constructor later on down the line, we can do this with the help of the prototype object
// Every time we create object or create the constructor for an object, there is a hidden object that exists within all of these. It is called the prototype object. By acessing the prototype object present within all 
// instances of an object, we can make edits to one object, and that edit applies to all object. Or we can make edits to the constructor shown below

Person.prototype.getFullName = function(){
	return `${this.firstName} ${this.lastName}`;
}

// Considering all the above there is a better, more easier way to create object instances and that is with classes. Now classes do the exact same thing as what we did, it just does it with different easier to read syntax

class Card {
	constructor(value, suit, color){
		this.value = value;
		this.suit = suit;
		this.color = color;

	}

	getSuit(){
		return this.suit;
	}

	getValue(){
		return this.value;
	}
}

const card1 = new Card(5, "Hearts", "blue");

console.log(card1);

console.log(card1.getValue());


/* Object oriented Programming */


// DOM stands for Document Object Model, which basically the structural layout of the webpage. DOM manipulation involves manipulation of the HTML of the webpage using JS
// Now for DOM manipulation we have a sample HTML page with completed CSS which we are going to use to use to demostrate the concepts

console.log(window); // The window object is the parent object of the browser. All the essential function/methords that are part of/use the window are present in this object

console.log(window.document); // The document is an object within the window object. The document object contains all the necessary functions/methods required for DOM manipulation

// single element seleector
console.log(document.getElementById("my-form")); // The getElementById method is used to refer or select a particular element in the HTML my referencing it's id. The id of the particular tag goes into the method input, and this method is used to select 
// only one element

const form = document.getElementById("my-form"); // We can even store certain elements in variables

console.log(document.querySelector(".container")) // This method is used to select/refer to elements by either their class or their tag name. To refer to a particular element that is of a certain class, we input the classname with a . preceding it to referto a class
// to refer to a certain tag, we use the tag name, however since this method is a single element selector, it is only going to refer to the first one

// multiple element selector
console.log(document.querySelectorAll(".item")); // This method is used to select multiple elements. If we input the name of a class (with a . before class name) in the method, then we will get an output of all the tags which are a part of that class.
// if we input the name of a tag in the method, we get the output of the tags which are that tag. If we input an id name (with a # before id name), the same logic applies
// This output will be in the form of a node list, which is kinda like an array (in fact we can run array methods on it). Every element in the array will contain tags which are part of the specified class, hence multiple tags gets selected.

const item = document.querySelectorAll(".item");

console.log(document.getElementsByClassName('item')); // This method is an old and outdated one, so don't bother to use it. This method selects a group of tags, by refering to their class name only. 
// Since we can only specify class name, this method is inferior to querySelectorAll. Also remember that when using this method we need to input class name with out the . before it, since this method only takes class input
// This method also returns multiple elements, but neither returns them in array nor node list form, it returns it in a HTML collecton form, which is an oudated datatype that does not allow array methords to be used on it.
// We would need to manually convert each of the HTML collections to arrays to use them as such.

console.log(document.getElementsByTagName("h1")); // This method is similar to the one above and is used to select multiple arrays which have same tahg name.

// Manipulation with selected elements

// We can loop through selected elements using array method/ for loops

item.forEach((item) => console.log(item));

const ul = document.querySelector(".items");

//ul.remove(); // This method removes the element that is currently selected, from the webpage

// ul.lastElementChild().remove(); // The method lastElementChild refers to/selects last element in the node list

ul.firstElementChild.textContent = "Hello"; // With the help of this element you can change the text content within an element

ul.children[1]; // We can also refer to an element in a node list by referncing it's index as shown here. We need to use the children method though

ul.children[1].innerText = "Sid"; // The innerText method can be used as an alternative to the textContent method

ul.lastElementChild; // This method is used to select the last element in a node list

ul.lastElementChild.innerHTML = "<h1> Vadyalam </h1>"; // This method is used to inject our own HTML into the selected element

// Dynamic events

const btn = document.querySelector(".btn");

btn.style.background = "red"; // We can even apply our own styling using JS

// An event is any instance where the user interacts with the webpage. We can create JS code that reacts to events which is shown below

btn.addEventListener("click", function(e){ // The event listener function moniters the webpage for events, such as clicks, swipes etc. We can specify what event we want it to look for by mentioning it as the first parameter of the method.
// The next parameter of the method is a function, that specifies what you want to happend when the event gets triggered.
	e.preventDefault(); // This prevents the default behavior of the tag
	console.log("click"); 
	// For the code shown here, whenever we click on the button tag the word "click", will only be printed out to the console for a split second. This is because the button here is a form submit button, and when clicked will
	// send a file containg the data from the form to a specified location. This is the default behavior of a submit button and is why the submit button gets activated for only a split second. If we want the word "click" to be 
	// printed out permanently we would have to disable the default behavior of the tag. This can be done with the method shown above

	console.log(e); // The variable e here called the event object. This object contains a lot of information related to the event, such as mouse position, the element that was clicked etc.
	console.log(e.target); // This method returns the tag that the mouse was present over when the event was triggered
	console.log(e.target.className); // We can add on further methods to this tag, such as getting the class name of the tag

	document.querySelector("#my-form").style.background = "#ccc"; // We can use events to manipulate the DOM. Here the background of the form is changing in response to the submit button getting pressed
	document.querySelector("body").classList.add('bg-dark'); // We can even change what class an element is in in response to an event. This can be done by adding or removing class names from the list of classes that the tag is apart of
	// The .remove() method added at the end of classList can remove the tag from that class
	document.querySelector(".items").lastElementChild.innerHTML = "<h1> JESUS IS KING </h1>"; // This changes the text in response to the event
})

btn.addEventListener("mouseover", function(a){ // This input to the event listener method, triggers the event when the mouse hovers over the tag
	console.log("hover");
})

btn.addEventListener("mouseout", function(a){ // This input to the event listener method, triggers the event when the mouse hovers out of the tag
	console.log("houver out");
})

btn.addEventListener("submit", function(a){ // This input to the event listener method, triggers the event when the form gets submitted
	console.log("submit");
})

/* DOM manipulation */


/* https://developer.mozilla.org/en-US/  Use this website to look at JavaScript Documentation */