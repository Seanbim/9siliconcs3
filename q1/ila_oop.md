# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

Encapsulation can be applied by creating a `Product` object that groups the product's name, price, and quantity together. The object can also have methods for actions such as adding or removing stock. This keeps the related data and methods organized within one object instead of using many separate variables.

### 2. Abstraction

Abstraction can be used to hide the details of how the inventory is updated. For example, the user can call an `addStock()` or `removeStock()` method without needing to know how the quantity is changed internally. This makes the inventory system simpler to use and understand.

### 3. Inheritance

Inheritance can be used when different types of products share the same properties and methods. For example, different product objects can inherit common properties such as name, price, and quantity from a `Product` object. This prevents the same properties and methods from having to be created repeatedly.

### 4. Polymorphism

Polymorphism can allow different product objects to use the same method while behaving differently. For example, different types of products could have their own version of a `displayInfo()` method. The same method can then be called for different objects while producing information appropriate to each product.

## Reflection

Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It would allow the name, price, and quantity of each product to be grouped into one object. This would make the program more organized and reduce the need for many separate variables. It would also keep the data and methods related to each product together.