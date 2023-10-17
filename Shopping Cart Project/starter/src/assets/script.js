// An empty array, which will later contain all the products in SKU
let products = [];

/*
  let product1: {
    name: "Carton of Cherries",
    price: 4,
    quantity: 0,
    productId: 1,
    image: "../images/cherry.jpg",
  };
  let product2: {
    name: "Carton of Strawberries",
    price: 5,
    quantity: 0,
    productId: 2,
    image: "../images/strawberry.jpg",
  };
  let product3: {
    name: "Bag of Oranges",
    price: 10,
    quantity: 0,
    productId: 3,
    image: "../images/orange.jpg",
  }
}


products.push(product1, product2, product3);
*/
/*
 A global object to contain all item in the SKU.
 Implemented this to allow code to import json (or csv) list 
 of products instead of hardcoding products into script.
 */
let globalProductList = {
  product1: {
    name: "Carton of Cherries",
    price: 4,
    quantity: 0,
    productId: 1,
    image: "../images/cherry.jpg",
  },
  product2: {
    name: "Carton of Strawberries",
    price: 5,
    quantity: 0,
    productId: 2,
    image: "../images/strawberry.jpg",
  },
  product3: {
    name: "Bag of Oranges",
    price: 10,
    quantity: 0,
    productId: 3,
    image: "../images/orange.jpg",
  }
};

// This converts the object (globalProductList) to an array
const productArray = Object.values(globalProductList);

/*
  Use the Array.forEach() to loop through items in the array
  productArray and push to the products list.
  */
productArray.forEach((element) => products.push(element));

/*
  An empty array, items and their quantities selected from the shelf
  are added to the card later on.
  */
let cart = [];

// Helper function: to get product by Id from product list
function getProductByIdFromList(productId, productList) {
  return productList.find((prod) => prod.productId === productId);
}

// Helper function: to get product by index from product list
function getProductByIndexFromList(productId, productList) {
  return productList.findIndex((prod) => prod.productId === productId);
}

/*
  A function to add a product to the cart
  Uses a helper function to add products to the list using the Id
  If product with the Id is not already in cart, 
    the product is added to the cart.
  If product already exists in the cart,
    the quantity of the product is increased by 1.
  */
function addProductToCart(productId) {
  let product = getProductByIdFromList(productId, products);
  if (product) {
    let existingCartItem = getProductByIdFromList(productId, cart);
    if (existingCartItem) {
      existingCartItem.quantity++;
    } else {
      cart.push({ ...product, quantity: 1 });
    }
  }
}

/*
  A function to add a product to the cart
  Uses a helper function to get product using the Id.
  Increases the quanity of the product by 1 every time 
    the function is called.
  */
function increaseQuantity(productId) {
  let product = getProductByIdFromList(productId, cart);
  if (product) {
    product.quantity++;
  }
}

/*
  Create a function to decrease the quantity of a product in the cart
  Uses a helper function to decrease products in the list using the Id.
  Decreases the quanity of the product by 1 every time 
    the function is called.
  */
function decreaseQuantity(productId) {
  let productIndex = getProductByIndexFromList(productId, cart);
  if (productIndex !== -1) {
    let product = cart[productIndex];
    if (product.quantity > 1) {
      product.quantity--;
    } else {
      cart.splice(productIndex, 1);
    }
  }
}

/*
  A function to remove a product from the cart
  Uses a helper function to decrease products in the list using the Id.
  Reassigns quantity of the product in the cart to zero '0' and
    subsequently remove the item.
  */
function removeProductFromCart(productId) {
  let productIndex = getProductByIndexFromList(productId, cart);
  if (productIndex !== -1) {
    cart[productIndex].quantity = 0;
    cart.splice(productIndex, 1);
  }
}

/*
  Function to calculate the total cost of the cart
  based on the items in the cart and their quantities.  
  */
function cartTotal() {
  let total = 0;
  for (let item of cart) {
    total += item.price * item.quantity;
  }
  return total;
}

/*
  Function to remove all items in the cart, regardless of their
  quantity based on the items in the cart and their quantities.  
  */
function emptyCart() {
  cart.forEach(function (product) {
    removeProductFromCart(product.productId);
  });
}

// Global variable to track payment installments
let totalPaid = 0

/*
  Function to check if total payment made is sufficient
  to clear their bills based on the worth of the cart (cartTotal)
    Empties the cart when full payment is made.
    Refunds a balance if payment exceeds the cartTotal
    else Cx keeps paying.
  */
function pay(amount) {
  totalPaid += amount;
  let total = cartTotal();
  balance = totalPaid - total;
  if (totalPaid >= total) {
    emptyCart();
  }
  return balance;
}

module.exports = {
  products,
  cart,
  addProductToCart,
  increaseQuantity,
  decreaseQuantity,
  removeProductFromCart,
  cartTotal,
  pay, 
  emptyCart,
  /* Uncomment the following line if completing the currency converter bonus */
  // currency
}
