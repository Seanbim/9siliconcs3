# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Skills
Description: it is abilities or powers used by users in a game.
## New Related Class
Class: Characters
Description: The game representation of a player and the object that uses skills
## Association
Relationship: Skill is utilized by Character
Explanation: A skill on it's own is just an ability—it only becomes useful when a character decides to cast it.
## Multiplicity

Multiplicity: 1 character --------- 0..* skills
Explanation: 1 character can obtain multiple skills, therefore it is one-to-many
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The original class, Skills, are the abilities used by the new class, Character.
### What multiplicity did you choose and why?
one-to-many because 1 skill can be learned by multiple characters.
### How did you implement the relationship in Python?
The character class stores the skils in self.skills, a list.
### Why did you store an object reference instead of copying its data?
Storing the object reference would mean that any changes made to the original skill is automatically reflected wherever it is referenced.
### If your relationship uses many, why is a list appropriate?
Because the amount of skills the character learns isn't fixed, they can learn as many as they want which makes the list important
