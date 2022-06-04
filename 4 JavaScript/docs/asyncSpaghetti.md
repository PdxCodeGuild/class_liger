# Async Spaghetti

## <a id="callbacks"></a>Callbacks

A callback function is a function that is passed as an argument to another function and is run when the operations of that function are completed.

```javascript

function sayHello(name){
    alert(`Hello ${name}`);
}

function getName(callback){
    let name = prompt('Please enter your name: ')
    callback(name);
}

getName(sayHello);
```

The previous code is an example of a **synchronous** callback, as it is executed immediately. 

However, callbacks are often used to continue code execution after an **asynchronous** operation has completed; these are called **asynchronous callbacks**.

Let's take the example of preparing spaghetti to demonstrate this idea.

<br>

```javascript
function makeSpaghetti(){
    const veggies = chopVeggies();
    const sauce = cookSauce();
    const water = boilWater();
    const noodles = cookNoodles();
    const spaghetti = assembleSpaghetti();

    return spaghetti
}

const spaghetti = makeSpaghetti()
eat(spaghetti)
```

<br>

In this code, we have a function which will carry out all the essential steps in preparing spaghetti. However, many of these steps take time to accomplish. If we tried to assemble the spaghetti before the sauce and noodles were fully cooked, our spaghetti would be crunchy garbage - unappetizing to say the least.

So, we'll have to wait for each step to be completed before undertaking the next step. If we want to wait for something in Javascript, we'll need to use a callback.

We can only start the sauce after the 

```javascript
function makeSpaghetti(ingredients) {
    chopVeggies(function(choppedVeggies)){
        // we can only use the veggies once they're prepared
    }
}
```

Once the veggies are chopped, we can begin to cook them. However, we'll have to wait for the sauce to be done before starting the water for our noodles. 

```javascript
function makeSpaghetti(ingredients) {
    chopVeggies(function(choppedVeggies)){
        cookSauce(function(cookedSauce){
            // now we can start the water 
        });
    };
};
```

Once the sauce is cooked, we can boil the water.

```javascript
function makeSpaghetti(ingredients) {
    chopVeggies(function(choppedVeggies){
        cookSauce(function(cookedSauce){
            boilWater(function(boilingWater){
                // now we can cook the noodles
            });
        });
    };
};
```

Once the water is boiling we can cook the noodles.

```javascript
function makeSpaghetti(ingredients) {
    chopVeggies(function(choppedVeggies){
        cookSauce(function(cookedSauce){
            boilWater(function(boilingWater){
                cookNoodles(function(alDenteNoodles){
                    // no we can assemble the spaghetti
                });
            });
        });
    };
};
```

Now we can assemble the spaghetti.

```javascript
function makeSpaghetti(ingredients) {
    chopVeggies(function(choppedVeggies){
        cookSauce(function(cookedSauce){
            boilWater(function(boilingWater){
                cookNoodles(function(alDenteNoodles){
                    assembleSpaghetti(function(){
                        // eat spaghetti
                    });
                });
            });
        });
    };
};
```

Finally we can eat the spaghetti. But, we can't return `spaghetti` from `assembleSpaghetti()`, because it is asynchronous. So, we have to pass one more callback to allow us to eat.

```javascript
function makeSpaghetti(ingredients, eatFunction) {
    chopVeggies(veggies, function(choppedVeggies){
        cookSauce(choppedVeggies, function(sauce){
            boilWater(sauce, function(boilingWater){
                cookNoodles(cookedNoodles, function(cookedNoodles){
                    assembleSpaghetti(cookedNoodles, sauce, function(nextStep){
                        const spaghetti = cookedNoodles + sauce;
                        eatFunction(spaghetti)
                    });
                });
            });
        });
    };
};

makeSpaghetti(ingredients, eat)
```

Yum! :spaghetti: 

Unfortunately, the code needed to make the spaghetti quickly starts to resemble spaghetti itself. 

Imagine if each of the callback functions had more complicated logic that spanned many lines. It would become a huge headache to reason through that mess. This situation is often referred to as "Callback Hell".

The callback functions could be cleaned up a bit by clever use of comments or by providing each callback a name, rather than writing them anonymously, but there are other, more streamlined solutions.

<br>
<br>

## <a id="promises"></a>Promises

The `Promise` object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.

A Promise is a placeholder for an unknown value that doesn't exist when the Promise is created.

We can attach callbacks to the Promise to handle the various outcomes of the operation we're performing and return the Promise from an asynchronous operation instead of the final value.

**Instead of immediately returning a value, the asychronous function returns a *promise* to supply a value later.**

Promises exist in one of three states:

- **pending** - initial state, neither fulfilled nor rejected
- **fulfilled** - indicates the operation was completed successfully
- **rejected** - indicates the operation failed

A pending promise can either be fulfilled with a value or rejected with a reason (error). 

The `Promise` constructor takes in a function with two parameters: `resolve` and `reject`. These are functions that will be called based on how the final outcome of the Promise.

When a Promise is returned from a function, the result of the `resolve()` and `reject()` functions can be handled using the Promise object's `.then()` and `.catch()` methods. Both methods take in a function as an argument which will be executed when the method is called.

If the Promise is resolved, `.then()` will be called with the resulting data. If the Promise is rejected `.catch()` will be called with the resulting error. 

`.then()` and `.catch()` both return new Promises of their own, so they can be chained. 

```javascript
asyncAction()
    .then(result => console.log(result))
    .then(newResult => console.log(newResult))
    .catch(error => console.error(error))
```

If written using Promises, our spaghetti example transforms into this:

```javascript
const chopVeggies = (veggies) => {
    return new Promise((resolve, reject)=>{
        if(!veggies){
            // if we've got veggies, chop them
            return resolve(choppedVeggies)
        } else {
            // if there was an error
            return reject(new Error("Oops! We need veggies to make sauce!"))
        }
    });
}

const cookSauce = (choppedVeggies) => {
    return new Promise((resolve, reject)=>{
        if(choppedVeggies){
            // if the veggies are chopped, cook them
            return resolve(sauce)
        } else {
            // if there was an error
            return reject(new Error("Oops! We need to chop the veggies first!"))
        }
    });
}

const boilWater = (sauce) => {
    return new Promise((resolve, reject) => {
        if(sauce){
            return resolve(boilingWater)
        } else {
            return reject(new Error('The sauce should be done before boiling the water.'))
        }
    });
}

const cookNoodles = (boilingWater, noodles) => {
    return new Promise((reject, resolve) => {
        if(boilingWater){
            return resolve(cookedNoodles)
        } else {
            return reject(new Error('The water needs to be boiling before cooking noodles'))
        }
    });
}

const assembleSpaghetti => (cookedNoodles, sauce) = {
    return new Promise((resolve, reject) => {
        if(cookedNoodles && sauce) {
            const spaghetti = cookedNoodles + sauce;
            return resolve(spaghetti)
        } else {
            return reject(new Error('Spaghetti needs noodle and sauce'))
        }
    })
}

// let's make the spaghetti with promises
const makeSpaghetti = (ingredients) => {
    // return a promise which will resolve when the spaghetti is done
    return chopVeggies(veggies)
        .then(choppedVeggies => cookSauce(choppedVeggies))
        .then(sauce => boilWater(sauce))
        .then(boilingWater => cookNoodles(boilingWater, noodles))
        .then(cookedNoodles => assembleSpaghetti(cookedNoodles, sauce))
}

// make the spaghetti and eat it when it's done
makeSpaghetti(ingredients)
    .then(spaghetti => eat(spaghetti))
    .catch(error => console.log(error))
```

As we can see, this cleans up the logic of making the spaghetti quite a bit. Since each of the helper functions returns a Promise, we can chain the processes together using `.then()` and they will only be performed once the previous process has finished successfully. If an error is encountered along the way, it can be handled using `.catch()`.

<br>
<br>

## <a id="async-await"></a>`async` / `await`

An `async` function is a function declared with the `async` keyword, and the `await` keyword is permitted within them. 

The `async` and `await` keywords enable asynchronous, promise-based behavior to be written in a cleaner style, avoiding the need to explicitly configure promise chains.

Placing the keyword `await` in front of a function that returns a Promise will cause the code to wait until the Promise is resolved or rejected before continuing. The resolved value of the Promise is then treated as the return value for the function.

Use of `async` and `await` allows us to use `try`/`catch` blocks around asynchronus code.

If we apply this concept to our spaghetti example, our `makeSpaghetti()` function could look something like this:

```javascript
const makeSpaghetti = async (veggies, noodles) => {
    const choppedVeggies = await chopVeggies(veggies);
    const sauce = await cookSauce(choppedVeggies);
    const boilingWater = await boilWater(sauce);
    const cookedNoodles = await cookNoodles(boilingWater, noodles);
    const spaghetti = await assembleSpaghetti(cookedNoodles, sauce);
    
    return spaghetti
}

// make spaghetti for dinner and eat it when it's done
const makeDinner = async () => {
    try {
        const dinner = await makeSpaghetti();
        eat(dinner);
    } catch error {
        console.log(error)
    }
}
```

Now the process looks more like synchronous code and will wait for each step to be accomplished before beginning the next. 

We can also use `try` / `catch` to handle any errors that happen along the way.

[Back to top](#top)
