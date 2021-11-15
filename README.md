# AirBnB clone - The console

![proyecto hbnb](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211111T204818Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=be7a5539edf138124cb3185cc110bc2983ba70ef0988ecd267e83bb04916824e)

## Table of Contents 🔍
1. Description
2. Objectives
3. How to use the command interpreter
4. How to work the command interpreter
6. Files and prototypes used for our program
7. Examples - how to use
8. Flowchart
9. Authors 

## 1. Description 📖
### What is AirBnB project?
With this project we intend to create our first complete web application: The AirBnb clone.

### AirBnB clone - The console
This is the first step: write a command interpreter to manage AirBnB objects.

![proyecto hbnb the console](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20211113%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211113T172113Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ef92c42fb55320a2eea35eae6628ccd009a761073b37922a8984e631a87a7a7a)

## 2.Objectives 🌈
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## 3. How to use the command interpreter ⌨️

To run our command interpreter you must use:
```
./console.py
```

The interactive mode ./console.py
```
$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

The non-interactive mode is, for example, when you type 
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```

## 4. How to work the command interpreter 💻 

### What is cmd module ?
The cmd module contains a public class, cmd, designed to be used as a base class for interactive shells and other command shells.
For this project we create the command interpreter using cmd, this interpreter uses a loop to read all the lines of its input, once analyzed it sends the command to an appropriate command controller.
The input lines are parsed in two parts: the command and any other text on the line.

Example:
The user enters $ create BaseModel, and the interpreter class includes a method called do_create (), it is executed with "BaseModel" as the only argument.

### Interpreter help

To display the interpreter help, you must enter the help command or the ? Character. The general help shows all the commands that the interpreter accepts.
You can also show the help of a specific command, by entering help command or ? command.
The help to display a command will be the documentation that contains its do_command method.

Example:
```
(hbnb)help create
 Creates a new instance of any of these classes:
        ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'Review', 'State']
        Ex: $create BaseModel 

(hbnb)? destroy
Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $destroy BaseModel 5500fd26-19a3-436d-b8e5-96f00670e0d4 
(hbnb)
```
## 5. Files and class used for our program 📚

DIRECTORY | FILES | DESCRIPTION |
| ------ | ------ | ------ |
| | console.py  | program called console.py that contains entry point of the command interpreter
| models/ | base_model.py | defines class BaseModel
| models/ | user.py, amenity.py, city.py, place.py, review.py, state.py | defines classes that inherit from BaseModel 
| models/engine/ | file_storage.py | Defines Class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.
| tests/ | test_models.py, test_console.py | all files, classes and functions are tested with unittest
 

# 6. Examples - how to use 🎉

Interactive mode 
Create a new object and display its string representation
```
$ ./console.py
(hbnb)create BaseModel
c02c6b72-7ae5-427a-aceb-4387a7d89c0d
(hbnb)show BaseModel c02c6b72-7ae5-427a-aceb-4387a7d89c0d
[BaseModel] (c02c6b72-7ae5-427a-aceb-4387a7d89c0d) {'id': 'c02c6b72-7ae5-427a-aceb-4387a7d89c0d', 'created_at': datetime.datetime(2021, 11, 13, 14, 48, 48, 402430), 'updated_at': datetime.datetime(2021, 11, 13, 14, 48, 48, 402450)}
```
Create a new User class object and display all objects
```
(hbnb)create User
273ff7db-0a35-4af0-b79f-0fb267073dd5
(hbnb)all
["[BaseModel] (c02c6b72-7ae5-427a-aceb-4387a7d89c0d) {'id': 'c02c6b72-7ae5-427a-aceb-4387a7d89c0d', 'created_at': datetime.datetime(2021, 11, 13, 14, 48, 48, 402430), 'updated_at': datetime.datetime(2021, 11, 13, 14, 48, 48, 402450)}", "[User] (273ff7db-0a35-4af0-b79f-0fb267073dd5) {'id': '273ff7db-0a35-4af0-b79f-0fb267073dd5', 'created_at': datetime.datetime(2021, 11, 13, 14, 49, 4, 122228), 'updated_at': datetime.datetime(2021, 11, 13, 14, 49, 4, 122246)}"]
```
Deletes an instance based on the class name and id
```
(hbnb)destroy User 273ff7db-0a35-4af0-b79f-0fb267073dd5
(hbnb)all
["[BaseModel] (c02c6b72-7ae5-427a-aceb-4387a7d89c0d) {'id': 'c02c6b72-7ae5-427a-aceb-4387a7d89c0d', 'created_at': datetime.datetime(2021, 11, 13, 14, 48, 48, 402430), 'updated_at': datetime.datetime(2021, 11, 13, 14, 48, 48, 402450)}"]
(hbnb)

```

## Authors ✒️
* Luisa Fernanda Pinillos  - [LuisaPinillos](https://github.com/LuisaPinillos)
* Laura Isabela Gómez - [IsabelaGomez101](https://github.com/IsabelaGomez101)
