"""What are some potential efficiency disadvantages of having very deep in-
heritance trees, that is, a large set of classes, A, B, C, and so on, such that
B extends A, C extends B, D extends C, etc.?"""
# A --> B --> C --> D --> etc

# obviously the more classes you have the large the code base becomes, thus keeping hard track of.

# quickly gain distance from the base class, alienating common attributes/methods.

# if one class breaks, all proceeding child classes can break. 





