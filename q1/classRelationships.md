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

Multiplicity: 1 skill --------- 0..* characters
Explanation: 1 skill can be obtained by multiple characters, therefore it is one-to-many
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
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
